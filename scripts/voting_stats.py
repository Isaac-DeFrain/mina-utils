#!/usr/bin/bash

import os
import json
import pathlib
import argparse
import statistics
from google.cloud import storage

# Steps
# 0. provide ledger hash
# 1. download ledger data from https://docs.minaexplorer.com/minaexplorer/data-archive/ledger_hash to local file
# 2. filter out essential fields for calculated stake: balance and delegate
# 3. aggregate each public key's stake
# 4. compute total stake
# 5. get voting data
# 6. stake-weight votes
# 7. aggregate votes

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'voting_service_key.json'
PARENT_DIR = pathlib.Path(__file__).parent
LOCAL_DATA_DIR = PARENT_DIR / "mina-explorer-data"
DATA_ARCHIVE = pathlib.Path('https://storage.googleapis.com/mina-explorer-ledgers/')

def data_loc(ledger_hash):
    return str(LOCAL_DATA_DIR / f"{ledger_hash}.json")

def download_ledger(ledger_hash):
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

# TODO stats
# total number of BPs?

def stats(agg_stake):
    total_stake = 0
    for v in agg_stake.values():
        total_stake += v
    print("\n~~~~~~~~~~~~~~")
    print("~ Statistics ~")
    print("~~~~~~~~~~~~~~")
    print("-- Votes")
    print(f"TODO yes")
    print(f"TODO no")
    print("-- Stake")
    print(f"Total : {total_stake}")
    print(f"Mean  : {statistics.mean(agg_stake.values())}")
    print(f"Stdev : {statistics.stdev(agg_stake.values())}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Vote aggregator")
    parser.add_argument("ledger_hash", type=str, nargs=1, help="ledger hash from which to compute the voting stake distribution")
    args = parser.parse_args()
    ledger_hash = args.ledger_hash[0]
    download_ledger(ledger_hash)
    ledger = parse_ledger(ledger_hash)
    agg_stake = aggregate_stake(ledger)
    stats(agg_stake)
