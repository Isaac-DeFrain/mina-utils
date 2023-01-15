import os
import sys
import json
import base58
import argparse
import mina_voting_graphql as mvg
import mina_voting_constants as mvc

def data_loc(fname):
    return mvc.LOCAL_DATA_DIR / f"{fname}.json"

#####################
# stake distribution
#####################

def get_next_staking_ledger_hash(epoch: int, endpoint: str) -> str:
    return mvg.get_next_ledger_hash(epoch + 1, endpoint)["data"]["blocks"][0]["protocolState"]["consensusState"]["nextEpochData"]["ledger"]["hash"]

def download_ledger(ledger_hash: str) -> list:
    """
    Downloads next staking ledger from https://github.com/Granola-Team/mina-ledger/tree/main/mainnet/
    """
    if not mvc.LOCAL_DATA_DIR.exists():
        os.mkdir(mvc.LOCAL_DATA_DIR)
    print(f"Downloading ledger with hash {ledger_hash} from {endpoint}...")
    mvg.get_next_staking_ledger_granola_github(ledger_hash)
    return raw_ledger_list

def filter_dict_keys(keys, dict: dict) -> dict:
    res = {}
    for k in keys:
        res[k] = dict[k]
    return res

def parse_ledger(raw_ledger: list) -> list:
    essential = ['balance', 'delegate']
    ledger = filter(lambda d: filter_dict_keys(essential, d), raw_ledger)
    return list(ledger)

def aggregate_stake(ledger: list, ep: int) -> dict:
    print("Aggregating stake...")
    agg_stake = {}
    delegators = set()
    for account in ledger:
        pk = account['pk']
        dg = account['delegate']
        bal = float(account['balance'])
        if pk != dg:
            delegators.add(pk)
        try:
            agg_stake[dg] += bal
        except KeyError:
            agg_stake[dg] = bal
    for d in delegators:
        try:
            del agg_stake[d]
        except KeyError:
            pass
    with mvc.aggr_stake_loc(ep).open("w", encoding="utf-8") as f:
        f.write(mvg.pp(agg_stake))
        f.close()
    return agg_stake

########
# votes
########

def get_block_heights_for_period(variables: dict, endpoint: str) -> list[int]:
    """
    Returns block heights for the given voting period
    """
    assert variables["min_date_time"] and variables["max_date_time"]
    raw_block_heights = mvg.get_block_heights(variables, endpoint)
    print(raw_block_heights)
    raw_block_heights = raw_block_heights["data"]["blocks"]
    return list(map(lambda d: d["blockHeight"], raw_block_heights))

def get_transactions_in_block(block_height: int, endpoint: str) -> list[dict]:
    """
    Returns the list of payment transactions in the given block
    """
    variables = {"block_height": block_height}
    return mvg.get_payments_in_block_height(variables, endpoint)["data"]["transactions"]

def download_transactions(variables: dict, ep: int, endpoint: str) -> dict:
    """
    Downloads transactions in voting period from the graphql `endpoint`
    """
    block_heights = get_block_heights_for_period(variables, endpoint)
    print(block_heights)
    print(f"Fetching blocks {block_heights[0]} - {block_heights[-1]}")
    print("This may take several minutes...")
    raw_tx_data = {}
    # TODO async fetching
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
    """
    Parses raw transaction data

    Returns raw votes (`memo` base58 encoded) and number of votes
    """
    num_txs = 0
    raw_votes = {}
    txns = []
    for block_height in per_block_tx_data.keys():
        txns += raw_tx_data[block_height]
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

#############
# statistics
#############

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
    Returns the lowercase, base58 decoded memo field
    '''
    memo = decode_memo(encoded_memo)
    return memo.lower()

def in_favor(encoded_memo, keyword) -> bool:
    memo = memo_of_vote(encoded_memo)
    if not memo:
        return False
    else:
        return memo == keyword

def against(encoded_memo, keyword) -> bool:
    memo = memo_of_vote(encoded_memo)
    if not memo:
        return False
    else:
        return memo == f'no {keyword}'

def pp_stake(stake_dist: dict, pk: str):
    try:
        return stake_dist[pk]
    except KeyError:
        return "delegated"

def results(agg_stake, votes, keyword, num_txs):
    """
    Tally vote weights for `keyword` and report results to stdout
    """
    no_votes = 0
    no_weight = 0
    yes_votes = 0
    yes_weight = 0
    stake_dist = {}
    total_vote_stake = 0

    # calculate total voting stake
    for v in votes:
        try:
            total_vote_stake += agg_stake[v[0]]
        except KeyError:
            pass

    # calculate stake distribution
    for v in votes:
        pk = v[0]
        try:
            stake_dist[pk] = agg_stake[pk] / total_vote_stake
        except KeyError:
            pass

    # tally stake-weighted votes
    for vote in votes:
        pk = vote[0]
        memo = vote[1]
        if pk in agg_stake.keys():
            if in_favor(memo, keyword):
                yes_votes += 1
                try:
                    yes_weight += stake_dist[pk]
                except KeyError:
                    pass
            elif against(memo, keyword):
                no_votes += 1
                try:
                    no_weight += stake_dist[pk]
                except KeyError:
                    pass
    # output results stats to stdout
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~ Voting Results ~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(f"~~~ Total ~~~")
    print(f"Num transactions: {num_txs}")
    print(f"Num yes votes:    {yes_votes}")
    print(f"Num no votes:     {no_votes}")
    print(f"Total vote stake: {total_vote_stake}")
    print()
    print(f"~~~ Votes ~~~")
    print(f"Yes vote weight:  {yes_weight}")
    print(f"No vote weight:   {no_weight}")

    if args.v:
        # print raw votes if verbose
        print()
        print("~~~~~~~~~~~~~~~~~")
        print("~~~ Raw votes ~~~")
        print("~~~~~~~~~~~~~~~~~")
        print(mvg.pp(dict(map(
            lambda v: (v[0], {
                "vote": memo_of_vote(v[1]),
                "stake": pp_stake(agg_stake, v[0]),
                "weight": pp_stake(stake_dist, v[0])
            }),
            votes
        ))))

######
# cli
######

def check(args: argparse.Namespace):
    # TODO multiple keywords
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
    parser.add_argument("-kw", type=str, nargs=1, help="keyword/MIP")
    parser.add_argument("-lh", type=str, nargs="*", help="ledger hash")
    parser.add_argument("-ep", type=int, nargs=1, help="voting epoch number")
    parser.add_argument("-start", type=str, nargs=1, help="voting period start time (in your local timezone) - ISO-8601 Y-m-dTH:M:SZ format")
    parser.add_argument("-end", type=str, nargs=1, help="voting period end time (in your local timezone) - ISO-8601 Y-m-dTH:M:SZ format")
    parser.add_argument("-gql", type=str, nargs="*", help=f"graphQL endpoint (default: {mvc.MINA_EXPLORER})")
    parser.add_argument("-v",  action="store_true", help="verbose")
    args = parser.parse_args()
    check(args)
    ep = int(args.ep[0])
    keyword = str(args.kw[0])
    endpoint = args.gql[0] if args.gql else mvc.MINA_EXPLORER
    variables = {
        "min_date_time": args.start[0],
        "max_date_time": args.end[0]
    }
    if not args.lh:
        ledger_hash = get_next_staking_ledger_hash(ep, endpoint)
    else:
        ledger_hash = get_next_staking_ledger_hash(ep, endpoint)
        if ledger_hash != args.lh[0]:
            print("⚠️ Mismatched next staking ledger hashes ⚠️")
            print(f"- provided via -lh: {args.lh[0]}")
            print(f"- downloaded: {ledger_hash}")
            sys.exit(1)
        else:
            print("Correct next staking ledger hash for epoch!")
    # only download the ledger if we don't already have it
    if not data_loc(ledger_hash).exists():
        raw_ledger_list = download_ledger(ledger_hash)
    else:
        with data_loc(ledger_hash).open("r", encoding="utf-8") as f:
            raw_ledger_list = json.load(f)
            f.close()
    ledger_list = parse_ledger(raw_ledger_list)
    # only aggregate stake if we haven't done so already
    if not mvc.aggr_stake_loc(ep).exists():
        agg_stake = aggregate_stake(ledger_list, ep)
    else:
        print(f"Reading aggregated from {mvc.aggr_stake_loc(ep)}")
        with mvc.aggr_stake_loc(ep).open("r", encoding="utf-8") as f:
            agg_stake = json.load(f)
            f.close()
    # only download the transactions if we don't already have them
    if not mvc.txns_loc(ep).exists():
        raw_tx_data = download_transactions(variables, ep, endpoint)
    else:
        with mvc.txns_loc(ep).open("r", encoding="utf-8") as f:
            raw_tx_data = json.load(f)
            f.close()
    votes, num_txs = parse_transactions(raw_tx_data, keyword)
    results(agg_stake, votes, keyword, num_txs)
