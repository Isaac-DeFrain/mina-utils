import pathlib

PARENT_DIR = pathlib.Path(__file__).parent

GITHUB_AUTH_TOKEN = PARENT_DIR / "voting_github_auth_token"

GRANOLA_LEDGER = "https://raw.githubusercontent.com/Granola-Team/mina-ledger/main/mainnet"

MINA_EXPLORER = "https://graphql.minaexplorer.com"
'''
Mina Explorer GraphQL endpoint
'''

def local_data_dir(ep: int) -> pathlib.Path:
    '''
    ./voting_data/epoch_{ep}
    '''
    return PARENT_DIR / f"voting-data/epoch_{ep}"

def aggr_stake_loc(ep: int):
    '''
    ./voting_data/epoch_{ep}/aggregated_stake.json
    '''
    return local_data_dir(ep) / f"aggregated_stake.json"

def txns_loc(ep: int):
    '''
    ./voting_data/epoch_{ep}/transactions.json
    '''
    return local_data_dir(ep) / f"transactions.json"

def ledger_loc(ep: int, ledger_hash: str) -> pathlib.Path:
    '''
    ./voting_data/epoch_{ep}/{ledger_hash}.json"
    '''
    return local_data_dir(ep) / f"{ledger_hash}.json"
