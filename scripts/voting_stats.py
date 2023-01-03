#!/usr/bin/bash

import os
import sys
import json
import base58
import argparse
import statistics
import voting_stats_graphql as vsg
import voting_stats_constants as vsc

# Steps
# 0. provide ledger hash
# 1. download ledger data from https://docs.minaexplorer.com/minaexplorer/data-archive/ledger_hash to local file
# 2. filter out essential fields for calculated stake: balance and delegate
# 3. aggregate each public key's stake
# 4. compute total stake
# 5. download relevant transaction data from https://graphql.minaexplorer.com GraphQL API
# 6. stake-weight votes
# 7. aggregate yes and no vote weights

# Granola's ledger data
# "https://raw.githubusercontent.com/Granola-Team/mina-ledger/main/mainnet/{}.json"

def data_loc(fname):
    return vsc.LOCAL_DATA_DIR / f"{fname}.json"

# stake distribution

def get_next_staking_ledger_hash(epoch: int, endpoint: str) -> str:
    return vsg.get_next_ledger_hash(epoch + 1, endpoint)["data"]["blocks"][0]["protocolState"]["consensusState"]["nextEpochData"]["ledger"]["hash"]

def download_ledger(ledger_hash: str, endpoint: str) -> list:
    """
    Downloads next staking ledger from `endpoint`
    """
    if not vsc.LOCAL_DATA_DIR.exists():
        os.mkdir(vsc.LOCAL_DATA_DIR)
    print(f"Downloading ledger with hash {ledger_hash} from Mina explorer...")
    raw_ledger_list = vsg.get_next_staking_ledger(ledger_hash, endpoint)["data"]["nextstakes"]
    with data_loc(ledger_hash).open("w", encoding="utf-8") as f:
        f.write(vsg.pp(raw_ledger_list))
        f.close()
    return raw_ledger_list

def filter_dict_keys(keys, dict: dict) -> dict:
    res = {}
    for k in keys:
        res[k] = dict[k]
    return res

def parse_ledger(raw_ledger: list) -> list:
    essential = ['balance', 'delegate']
    ledger = filter(lambda d: filter_dict_keys(essential, d), raw_ledger_list)
    return list(ledger)

def aggregate_stake(ledger: list) -> dict:
    print("Aggregating stake...")
    res = {}
    for account in ledger:
        dg = account['delegate']
        bal = float(account['balance'])
        if bal > 0:
            try:
                res[dg]
            except KeyError:
                res[dg] = 0
            res[dg] += bal
    with vsc.AGGREGATED_STAKE.open("w", encoding="utf-8") as f:
        f.write(vsg.pp(res))
        f.close()
    return res

# votes

def get_block_heights_for_period(variables: dict, endpoint: str) -> list[int]:
    """
    Returns block heights for the given voting period
    """
    assert variables["min_date_time"] and variables["max_date_time"]
    raw_block_heights = vsg.get_block_heights(variables, endpoint)["data"]["blocks"]
    return list(map(lambda d: d["blockHeight"], raw_block_heights))

def get_transactions_in_block(block_height: int, endpoint: str) -> list[dict]:
    """
    Returns the list of payment transactions in the given block
    """
    variables = {"block_height": block_height}
    return vsg.get_payments_in_block_height(variables, endpoint)["data"]["transactions"]

def download_transactions(variables: dict, endpoint: str) -> dict:
    """
    Downloads transactions in voting period from the graphql `endpoint`
    """
    block_heights = get_block_heights_for_period(variables, endpoint)
    print(f"Fetching blocks {block_heights[0]} - {block_heights[-1]}")
    print("This may take several minutes...")
    raw_tx_data = {}
    # TODO async fetching
    for height in block_heights:
        raw_tx_data[height] = get_transactions_in_block(height, endpoint)
        print(f"Got block {height}")
    with vsc.TRANSACTIONS.open("w", encoding="utf-8") as f:
        f.write(vsg.pp(raw_tx_data))
        f.close()
    return raw_tx_data

def is_vote(raw_tx: dict) -> bool:
    return all([
        raw_tx["memo"],
        raw_tx["kind"] == 'PAYMENT',
        raw_tx["source"]["publicKey"] == raw_tx["receiver"]["publicKey"]
    ])

def is_delegation(raw_tx: dict) -> bool:
    return raw_tx["kind"] == 'STAKE_DELEGATION'

def parse_transactions(raw_tx_data: dict) -> tuple[list, dict, int]:
    """
    Parses raw transaction data

    Returns raw votes (`memo` base58 encoded) and delegations { delegate_pk : delegated_balance }
    """
    num_txs = 0
    raw_votes = {}
    delegations = {}
    txns = []
    for block_height in raw_tx_data.keys():
        txns += raw_tx_data[block_height]
    for tx in txns:
        num_txs += 1
        pk = tx["source"]["publicKey"]
        if is_vote(tx):
            raw_votes[pk] = tx["memo"]
        elif is_delegation(tx):
            delegations[pk] = tx["receiver"]["publicKey"]
        raw_votes[pk] = tx["memo"]
    raw_voting = []
    for k in raw_votes.keys():
        raw_voting.append((k, raw_votes[k]))
    return raw_voting, delegations, num_txs

# statistics

def trim_bytes(bs: bytes) -> bytes:
    res = []
    for b in bs:
        if b:
            res.append(b)
    return bytes(res)

def unpad_base58(b58_encoded: bytes) -> str:
    if not b58_encoded[:3] == b"\x14\x01\x00":
        n = b58_encoded[2]
        memo = b58_encoded[3:]
        memo = memo[:-(n + 1)]
        return trim_bytes(memo).decode('utf8')
    else:
        return ""

def memo_of_vote(vote: tuple) -> str:
    memo = base58.b58decode(f'{vote[1]}')
    memo = unpad_base58(memo)
    return memo.lower() # no .strip()

def in_favor(vote, keyword) -> bool:
    memo = memo_of_vote(vote)
    if not memo:
        return False
    else:
        return memo == keyword

def against(vote, keyword) -> bool:
    memo = memo_of_vote(vote)
    if not memo:
        return False
    else:
        return memo == f'no {keyword}'

# TODO unique votes
# - highest block
# - heighest nonce if same block
def stats(agg_stake, votes, keyword, delegations, num_txs):
    """
    Tally vote weights for `keyword` and report statistics
    """
    no_votes = 0
    no_weight = 0
    yes_votes = 0
    yes_weight = 0
    total_stake = 0
    stake_dist = {}
    for v in agg_stake.values():
        total_stake += v
    for pk in agg_stake.keys():
        stake_dist[pk] = agg_stake[pk] / total_stake
    for vote in votes:
        if in_favor(vote, keyword):
            yes_votes += 1
            try:
                yes_weight += stake_dist[vote[0]]
            except:
                # pass
                # TODO remove
                print(f"{vote[0]} not found in ledger")
        elif against(vote, keyword):
            no_votes += 1
            try:
                no_weight += stake_dist[vote[0]]
            except:
                # pass
                # TODO remove
                print(f"{vote[0]} not found in ledger")

    print()
    print("~~~~~~~~~~~~~~~~~~")
    print("~~~ Statistics ~~~")
    print("~~~~~~~~~~~~~~~~~~")
    print(f"~~~ Total ~~~")
    print(f"Num transactions: {num_txs}")
    print(f"Num delegations:  {len(delegations)}")
    print(f"Num yes votes:    {yes_votes}")
    print(f"Num no votes:     {no_votes}")
    print(f"Num votes:        {len(votes)}")
    print(f"~~~ Votes ~~~")
    print(f"Yes vote weight:  {yes_weight} ({yes_votes})")
    print(f"No vote weight:   {no_weight} ({no_votes})")
    print(f"~~~ Stake ~~~")
    print(f"Total stake:      {total_stake}")
    print(f"Mean stake:       {statistics.mean(agg_stake.values())}")
    print(f"Stdev:            {statistics.stdev(agg_stake.values())}")
    if args.v:
        print("~~~ Votes ~~~")
        print(vsg.pp(dict(map(lambda v: (v[0], memo_of_vote(v)), votes))))

def check(args: argparse.Namespace) -> bool:
    if not args.kw:
        print("must provide a voting keyword via -kw")
        sys.exit(1)
    if not args.start:
        print("must provide a start time for the voting period via -start")
        sys.exit(1)
    if not args.end:
        print("must provide an end time for the voting period via -end")
        sys.exit(1)
    return any([
        args.lh and not args.ep,
        args.ep and not args.lh
    ])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Mina on-chain voting results calculator")
    parser.add_argument("-kw", type=str, nargs=1, help="keyword/MIP")
    parser.add_argument("-lh", action="store_true", help="ledger hash")
    parser.add_argument("-ep", action="store_true", help="voting epoch number")
    parser.add_argument("-v",  action="store_true", help="verbose")
    parser.add_argument("-gq", type=str, nargs="*", help=f"graphQL endpoint (default: {vsc.MINA_EXPLORER})")
    parser.add_argument("-start", type=str, nargs=1, help="voting period start time (in your local timezone) - ISO-8601 Y-m-dTH:M:SZ format")
    parser.add_argument("-end", type=str, nargs=1, help="voting period end time (in your local timezone) - ISO-8601 Y-m-dTH:M:SZ format")
    parser.add_argument("input", help="captures epoch or ledger hash")
    args = parser.parse_args()
    check(args)
    keyword = args.kw[0]
    endpoint = args.gq[0] if args.gq else vsc.MINA_EXPLORER
    variables = {
        "min_date_time": args.start[0] if args.start else vsc.START_TIME,
        "max_date_time": args.end[0] if args.end else vsc.END_TIME
    }
    if args.lh:
        ledger_hash = str(args.input)
    else:
        # args.ep
        ledger_hash = get_next_staking_ledger_hash(int(args.input), endpoint)
    # only download the ledger if we don't already have it
    if not data_loc(ledger_hash).exists():
        raw_ledger_list = download_ledger(ledger_hash, endpoint)
    else:
        with data_loc(ledger_hash).open("r", encoding="utf-8") as f:
            raw_ledger_list = json.load(f)
            f.close()
    print(f"Using endpoint: {endpoint}")
    ledger_list = parse_ledger(raw_ledger_list)
    # only aggregate stake if we haven't done so already
    if not vsc.AGGREGATED_STAKE.exists:
        agg_stake = aggregate_stake(ledger_list)
    else:
        with vsc.AGGREGATED_STAKE.open("r", encoding="utf-8") as f:
            agg_stake = json.load(f)
            f.close()
    # only download the transactions if we don't already have them
    if not vsc.TRANSACTIONS.exists():
        raw_tx_data = download_transactions(variables, endpoint)
    else:
        with vsc.TRANSACTIONS.open("r", encoding="utf-8") as f:
            raw_tx_data = json.load(f)
            f.close()
    raw_votes, delegations, num_txs = parse_transactions(raw_tx_data)
    votes = list(filter(lambda v: memo_of_vote(v), raw_votes))
    stats(agg_stake, votes, keyword, delegations, num_txs)
