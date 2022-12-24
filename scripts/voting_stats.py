#!/usr/bin/bash

import os
import json
import base58
import asyncio
import pathlib
import argparse
import statistics
from google.cloud import storage
from python_graphql_client import GraphqlClient
from voting_stats_constants import LOCAL_DATA_DIR, START_TIME, END_TIME

# Steps
# 0. provide ledger hash
# 1. download ledger data from https://docs.minaexplorer.com/minaexplorer/data-archive/ledger_hash to local file
# 2. filter out essential fields for calculated stake: balance and delegate
# 3. aggregate each public key's stake
# 4. compute total stake
# 5. download relevant transaction data from https://graphql.minaexplorer.com GraphQL API
# 6. stake-weight votes
# 7. aggregate yes and no vote weights

def data_loc(ledger_hash):
    return str(LOCAL_DATA_DIR / f"{ledger_hash}.json")

# stake

def download_ledger_to_local_file(ledger_hash):
    """
    Downloads ledger from Mina explorer
    """
    if not LOCAL_DATA_DIR.exists():
        os.mkdir(LOCAL_DATA_DIR)
    print(f"Downloading ledger with hash {ledger_hash} from Mina explorer...")
    bucket_name = "mina-explorer-ledgers"
    fname = ledger_hash + ".json"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(fname)
    blob.download_to_filename(data_loc(ledger_hash))
    print("Downloaded successful!")
    print(f"Writing to local file ../{fname}")

def filter_dict_keys(keys, dict):
    res = {}
    for k in keys:
        res[k] = dict[k]
    return res

def parse_ledger(ledger_hash):
    fname = data_loc(ledger_hash)
    with open(fname, "r") as f:
        accounts = json.load(f)
        f.close()
    essential = ['balance', 'delegate']
    ledger = filter(lambda d: filter_dict_keys(essential, d), accounts)
    return list(ledger)

def aggregate_stake(ledger):
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
    print("Writing aggregated stake to local file...")
    fpath = LOCAL_DATA_DIR / "aggregated-stake.json"
    with fpath.open("w") as f:
        json.dump(res, f, indent=4)
        f.close()
    return res

# votes

def download_transactions(endpoint, start_time=START_TIME, end_time=END_TIME):
    """
    Downloads transactions in voting period beginning at `start_time`
    and ending at `end_time` from the graphql `endpoint`
    """
    # gql_client = GraphqlClient(endpoint) #, headers=hdrs)
    # query_all_txs_in_voting_period = '''{
    #     transactions(query: {
    #         dateTime_gte: "%s",
    #         dateTime_lte: "%s"
    #     },
    #     sortBy: DATETIME_DESC
    #     ) {
    #         dateTime
    #         kind
    #         memo
    #         receiver {
    #             publicKey
    #         }
    #         source {
    #             publicKey
    #         }
    #     }
    # }''' % (start_time, end_time)
    # try:
    #     raw_tx_data = asyncio.run(gql_client.execute_async(query=query_all_txs_in_voting_period))
    # except:
    #     raw_tx_data = {"error" : "invalid content type"}
    fpath = LOCAL_DATA_DIR / "transactions.json"
    # with fpath.open("w") as f:
    #     f.write(json.dumps(raw_tx_data, indent=4))
    #     f.close()
    # return raw_tx_data
    with fpath.open("r") as f:
        txs = json.load(f)
        f.close()
    return txs

def is_vote(raw_tx):
    return all([
        raw_tx["memo"],
        raw_tx["kind"] == 'PAYMENT',
        raw_tx["source"]["publicKey"] == raw_tx["receiver"]["publicKey"]
    ])

def is_delegation(raw_tx):
    return raw_tx["kind"] == 'STAKE_DELEGATION'

def parse_transactions(raw_tx_data):
    """
    Parses raw transaction data

    Returns raw votes (`memo` base58 encoded) and delegations { sender_pk : receiver_pk }
    """
    num_txs = 0
    raw_votes = {}
    delegations = {}
    for tx in raw_tx_data["data"]["transactions"]:
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

def trim_bytes(bs):
    res = []
    for b in bs:
        if b:
            res.append(b)
    return bytes(res)

def unpad_base58(b58_encoded):
    if not b58_encoded[:3] == b"\x14\x01\x00":
        n = b58_encoded[2]
        memo = b58_encoded[3:]
        memo = memo[:-(n + 1)]
        return trim_bytes(memo).decode('utf8')
    else:
        return ""

def memo_of_vote(vote):
    memo = base58.b58decode(f'{vote[1]}')
    memo = unpad_base58(memo)
    return memo

def in_favor(vote, keyword):
    memo = memo_of_vote(vote)
    if not memo:
        return False
    else:
        return memo.lower() == keyword.lower()

def against(vote, keyword):
    memo = memo_of_vote(vote)
    if not memo:
        return False
    else:
        return memo.lower() == f'no {keyword.lower()}'

def stats(agg_stake, votes, keyword, delegations, num_txs):
    """
    Tally votes for `keyword` and report statistics
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
                pass
        elif against(vote, keyword):
            no_votes += 1
            try:
                no_weight += stake_dist[vote[0]]
            except:
                pass

    print("")
    print("~~~~~~~~~~~~~~")
    print("~ Statistics ~")
    print("~~~~~~~~~~~~~~")
    print(f"~ Total ~")
    print(f"Num transactions: {num_txs}")
    print(f"Num votes:        {len(votes)}")
    print(f"Num delegations:  {len(delegations)}")
    print(f"~ Votes ~")
    print(f"Yes vote weight:  {yes_weight} ({yes_votes})")
    print(f"No vote weight:   {no_weight} ({no_votes})")
    print(f"~ Stake ~")
    print(f"Total stake:      {total_stake}")
    print(f"Mean stake:       {statistics.mean(agg_stake.values())}")
    print(f"Stdev:            {statistics.stdev(agg_stake.values())}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Vote aggregator")
    parser.add_argument("-lh", type=str, nargs=1, help="ledger hash")
    parser.add_argument("-kw", type=str, nargs=1, help="keyword")
    parser.add_argument("-gq", type=str, nargs="*", help="graphQL endpoint")
    args = parser.parse_args()
    ledger_hash = args.lh[0]
    keyword = args.kw[0]
    endpoint = args.gq[0] if args.gq else "https://graphql.minaexplorer.com"
    if not pathlib.Path(data_loc(ledger_hash)).exists():
        download_ledger_to_local_file(ledger_hash)
    print(f"Using graphql endpoint: {endpoint}")
    ledger = parse_ledger(ledger_hash)
    agg_stake = aggregate_stake(ledger)
    raw_tx_data = download_transactions(endpoint)
    raw_votes, delegations, num_txs = parse_transactions(raw_tx_data)
    votes = list(filter(lambda v: memo_of_vote(v) != '', raw_votes))
    stats(agg_stake, votes, keyword, delegations, num_txs)
