import os
import sys
import json
import base58
import argparse
import mina_voting_graphql as mvg
import mina_voting_constants as mvc

#####################
# stake distribution
#####################

def get_next_staking_ledger_hash(epoch: int, endpoint: str) -> str:
    return mvg.get_next_ledger_hash(epoch + 1, endpoint)["data"]["blocks"][0]["protocolState"]["consensusState"]["nextEpochData"]["ledger"]["hash"]

def download_ledger(ledger_hash: str, endpoint: str) -> list:
    '''
    Downloads next staking ledger from https://github.com/Granola-Team/mina-ledger/tree/main/mainnet/
    '''
    if not mvc.LOCAL_DATA_DIR.exists():
        os.mkdir(mvc.LOCAL_DATA_DIR)
    print(f"Downloading ledger with hash {ledger_hash} from {endpoint}...")
    mvg.get_next_staking_ledger_granola_github(ledger_hash)
    with data_loc(ledger_hash).open('r', encoding='utf8') as f:
        raw_ledger_list = json.load(f)
        f.close()
    return raw_ledger_list

def parse_ledger(raw_ledger: list) -> list:
    '''
    Returns the list of (balance, delegate)-dicts
    '''
    essential = ['balance', 'delegate']
    ledger = filter(lambda d: filter_dict_keys(essential, d), raw_ledger)
    return list(ledger)

def aggregate_stake(ledger: list, ep: int, verbose: bool = False) -> dict:
    '''
    Returns 
    '''
    if verbose:
        print("Aggregating stake...")

    agg_stake = {}
    self_delegations = {}
    non_self_delegations = {}

    for account in ledger:
        pk = account['pk']
        dg = account['delegate']
        bal = float(account['balance'])

        # separate delegator types
        if pk == dg:
            self_delegations[pk] = dg
        else:
            non_self_delegations[pk] = dg

        # sum delegated balance
        try:
            agg_stake[dg] += bal
        except:
            agg_stake[dg] = bal

    # filter non-self delegators from agg stake
    for d in non_self_delegations.keys():
        try:
            del agg_stake[d]
        except:
            pass

    # write agg stake to aggr_stake_loc(ep)
    with mvc.aggr_stake_loc(ep).open("w", encoding="utf-8") as f:
        f.write(mvg.pp(agg_stake))
        f.close()

    return agg_stake

########
# votes
########

def get_block_heights_for_period(variables: dict, endpoint: str) -> list[int]:
    '''
    Returns block heights for the given voting period
    '''
    assert variables["min_date_time"] and variables["max_date_time"]
    raw_block_heights = mvg.get_block_heights(variables, endpoint)
    print(raw_block_heights)
    raw_block_heights = raw_block_heights["data"]["blocks"]
    return list(map(lambda d: d["blockHeight"], raw_block_heights))

def get_transactions_in_block(block_height: int, endpoint: str) -> list[dict]:
    '''
    Returns the list of payment transactions in the given block
    '''
    variables = {"block_height": block_height}
    return mvg.get_payments_in_block_height(variables, endpoint)["data"]["transactions"]

def download_transactions(variables: dict, ep: int, endpoint: str) -> dict:
    '''
    Downloads transactions in voting period from the graphql `endpoint`
    '''
    block_heights = get_block_heights_for_period(variables, endpoint)
    print(block_heights)
    print(f"Fetching blocks {block_heights[0]} - {block_heights[-1]}")
    print("This may take several minutes...")
    raw_tx_data = {}
    for height in block_heights:
        raw_tx_data[height] = get_transactions_in_block(height, endpoint)
        print(f"Got block {height}")
    with mvc.txns_loc(ep).open("w", encoding="utf-8") as f:
        f.write(mvg.pp(raw_tx_data))
        f.close()
    return raw_tx_data

def is_vote(raw_tx: dict, keyword: str) -> bool:
    return all([
        in_favor(raw_tx["memo"], keyword) or against(raw_tx["memo"], keyword),
        raw_tx["source"]["publicKey"] == raw_tx["receiver"]["publicKey"]
    ])

def parse_transactions(per_block_tx_data: dict, keyword: str) -> tuple[list, int]:
    '''
    Parses raw transaction data

    Returns raw votes (`memo` base58 encoded) and number of votes
    '''
    num_txs = 0
    raw_votes = {}
    txns = []
    for block_height in per_block_tx_data.keys():
        txns += per_block_tx_data[block_height]
    for tx in txns:
        num_txs += 1
        pk = tx["source"]["publicKey"]
        if is_vote(tx, keyword):
            memo = tx["memo"]
            height = tx["blockHeight"]
            nonce = tx["nonce"]
            try:
                v = raw_votes[pk]
                if v[1] < height or v[1] == height and v[2] < nonce:
                    raw_votes[pk] = [memo, height, nonce]
                else:
                    pass
            except KeyError:
                raw_votes[pk] = [memo, height, nonce]
    raw_voting = []
    for pk in raw_votes.keys():
        raw_voting.append([pk] + raw_votes[pk])
    return raw_voting, num_txs

##########
# results
##########

def get_account(ledger: list, pubkey: str) -> dict:
    res = {}
    for account in ledger:
        pk = account['pk']
        if pk == pubkey:
            res = account
            break
    return res

def display(res: dict, test: bool = False):
    '''
    Print results to stdout
    '''

    ledger = res['ledger']
    num_txns = res['num']
    votes, yes_votes, no_votes = res['votes']
    vote_weight, yes_weight, no_weight = res['weight']
    agg_stake, total_vote_stake = res['stake']
    
    if not test:
        # print report
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~ Voting Results Report ~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print(f"Keyword: {key[0]}")
        print()
        print(f">>> Totals")
        print(f"Num epoch txns: {num_txns}")
        print(f"Num yes votes:  {yes_votes}")
        print(f"Num no votes:   {no_votes}")
        print(f"Vote stake:     {total_vote_stake}")
        print()
        print(f">>> Weights")
        print(f"Yes vote weight: {yes_weight}")
        print(f"No vote weight:  {no_weight}")
        print()

        # print raw votes if verbose
        if args.v:
            print(">>> Voting details")
            print(mvg.pp(dict(map(
                lambda v: (v[0], {
                    "vote": memo_of_vote(v[1]),
                    "stake": weight_or_delegation(ledger, agg_stake, v[0], True),
                    "weight": weight_or_delegation(ledger, vote_weight, v[0], False)
                }),
                votes
            ))))

def calculate(args, test: bool = False) -> dict[str, list]:
    '''
    Calculates args for `results` (`agg_stake`, `votes`, `keyword`, `num_txns`)
    '''

    # given/default inputs
    ep = args.ep[0]
    keyword = args.kw[0]
    endpoint = args.gql[0] if args.gql else mvc.MINA_EXPLORER
    ledger_hash = args.lh[0] if args.lh else None
    variables = {
        "min_date_time": args.start[0],
        "max_date_time": args.end[0]
    }

    # download next staking ledger hash
    try:
        ledger_hash = get_next_staking_ledger_hash(ep, endpoint)
    except:
        print("FAILED: next staking ledger hash")
        sys.exit(1)

    # check if provided ledger hash matches downloaded
    if args.lh:
        if ledger_hash != args.lh[0]:
            print("⚠️ Mismatched ⚠️")
            print(f"- provided hash: {args.lh[0]}")
            print(f"- download hash: {ledger_hash}")
            sys.exit(1)
        else:
            print(f"Correct next staking ledger hash for epoch {ep}")

    # only download the ledger if we don't already have it
    if not data_loc(ledger_hash).exists():
        raw_ledger_list = download_ledger(ledger_hash, endpoint)
    else:
        with data_loc(ledger_hash).open("r", encoding="utf-8") as f:
            raw_ledger_list = json.load(f)
            f.close()

    # parse the raw ledger list
    ledger_list = parse_ledger(raw_ledger_list)

    # only aggregate stake if we haven't done so already
    if not mvc.aggr_stake_loc(ep).exists():
        agg_stake = aggregate_stake(ledger_list, ep)
    else:
        # otherwise read from local file
        with mvc.aggr_stake_loc(ep).open("r", encoding="utf-8") as f:
            agg_stake = json.load(f)
            f.close()

    # only download the transactions if we don't already have them
    if not mvc.txns_loc(ep).exists():
        raw_tx_data = download_transactions(variables, ep, endpoint)
    else:
        # otherwise read from local file
        with mvc.txns_loc(ep).open("r", encoding="utf-8") as f:
            raw_tx_data = json.load(f)
            f.close()

    # parse transactions and display results
    votes, num_txns = parse_transactions(raw_tx_data, keyword)
    return results(ledger_list, agg_stake, votes, keyword, num_txns)

def results(ledger_list, agg_stake, votes, keyword, num_txns) -> dict[str, list]:
    '''
    Returns all results `num`, `stake`, `votes`, `weight`
    '''

    # set initial values
    no_votes = 0
    no_weight = 0
    yes_votes = 0
    yes_weight = 0
    vote_weight = {}
    total_vote_stake = 0

    # calculate total voting stake
    for vote in votes:
        try:
            total_vote_stake += agg_stake[vote[0]]
        except:
            pass

    # calculate vote weights
    for vote in votes:
        try:
            pk = vote[0]
            vote_weight[pk] = agg_stake[pk] / total_vote_stake
        except:
            pass

    # tally stake-weighted votes
    for vote in votes:
        pk = vote[0]
        memo = vote[1]

        if pk in agg_stake.keys():

            # sum yes weight
            if in_favor(memo, keyword):
                yes_votes += 1
                try:
                    yes_weight += vote_weight[pk]
                except:
                    pass

            # sum no weight
            elif against(memo, keyword):
                no_votes += 1
                try:
                    no_weight += vote_weight[pk]
                except:
                    pass
    return {
        'num':    num_txns,
        'key':    [keyword],
        'stake':  [agg_stake, total_vote_stake],
        'votes':  [votes, yes_votes, no_votes],
        'weight': [vote_weight, yes_weight, no_weight],
        'ledger': ledger_list,
    }


##########
# helpers
##########

def data_loc(fname):
    return mvc.LOCAL_DATA_DIR / f"{fname}.json"

def filter_dict_keys(keys, dict: dict) -> dict:
    res = {}
    for k in keys:
        res[k] = dict[k]
    return res

# memo

def decode_memo(b58_encoded: str) -> str:
    '''
    Returns the base58 decoded input
    '''
    decoded = base58.b58decode(b58_encoded)
    if decoded[1] == b'x01':
        res = ""
    else:
        end_idx = decoded[2] + 3
        memo = decoded[3:end_idx]
        res = memo.decode('utf-8')
    return res

def memo_of_vote(encoded_memo: str) -> str:
    '''
    Returns the lowercase base58 decoded memo field
    '''
    memo = decode_memo(encoded_memo)
    return memo.lower()

# vote

def in_favor(encoded_memo, keyword) -> bool:
    '''
    Is this a vote in favor of the proposal?
    '''
    memo = memo_of_vote(encoded_memo)
    if not memo:
        return False
    else:
        return memo == keyword

def against(encoded_memo, keyword) -> bool:
    '''
    Is this a vote against the proposal?
    '''
    memo = memo_of_vote(encoded_memo)
    if not memo:
        return False
    else:
        return memo == f'no {keyword}'

def weight_or_delegation(ledger: list, dist: dict, pk: str, type: bool):
    '''
    Returns `pk`'s stake weight or the public key `pk` delegated to
    '''
    try:
        return dist[pk]
    except:
        if type:
            return get_account(ledger, pk)['delegate']
        else:
            return "N/A"

######
# cli
######

def check(args: argparse.Namespace):
    '''
    Validate the args
    '''
    if not args.ep:
        print("must provide an epoch number via -ep")
        sys.exit(1)
    if not args.kw:
        print("must provide a voting keyword via -kw")
        sys.exit(1)
    if not args.start:
        print("must provide a start time for the voting period via -start")
        sys.exit(1)
    if not args.end:
        print("must provide an end time for the voting period via -end")
        sys.exit(1)
    if args.lh and len(args.lh) > 1:
        print("can provide at most one ledger hash via -lh")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Mina on-chain voting results calculator")
    parser.add_argument("-kw", type=str, nargs=1, help="MIP keyword")
    parser.add_argument("-ep", type=int, nargs=1, help="Voting epoch number")
    parser.add_argument("-lh", type=str, nargs="*", help="Staking ledger hash")
    parser.add_argument("-start", type=str, nargs=1, help="Voting period start time (in your local timezone) - ISO-8601 YY-mm-ddTHH:MM:SS")
    parser.add_argument("-end", type=str, nargs=1, help="Voting period end time (in your local timezone) - ISO-8601 YY-mm-ddTHH:MM:SSZ")
    parser.add_argument("-v",  action="store_true", help="Verbose - shows all votes with memos decoded")
    parser.add_argument("-gql", type=str, nargs="*", help=f"GraphQL endpoint (default: {mvc.MINA_EXPLORER})")

    # validate args
    args = parser.parse_args()
    check(args)

    # calculate result args
    res = calculate(args)
    num = res['num']
    key = res['key']
    stake = res['stake']
    votes = res['votes']
    weight = res['weight']
    ledger = res['ledger']

    # display results
    display(results(list(ledger), stake[0], votes[0], key[0], num))
