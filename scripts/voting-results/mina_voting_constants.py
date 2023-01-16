import pathlib

PARENT_DIR = pathlib.Path(__file__).parent

GITHUB_AUTH_TOKEN = PARENT_DIR / "voting_github_auth_token"

GRANOLA_LEDGER = "https://raw.githubusercontent.com/Granola-Team/mina-ledger/main/mainnet"

MINA_EXPLORER = "https://graphql.minaexplorer.com"
'''
Mina Explorer GraphQL endpoint
'''

def local_data(ep: int, fname: str) -> pathlib.Path:
    '''
    ./voting_data/epoch_{ep}
    '''
    return PARENT_DIR / f"voting-data/epoch_{ep}"

def agg_stake_loc(ep: int) -> pathlib.Path:
    return local_data(ep, "aggregated_stake")

def txns_loc(ep: int) -> pathlib.Path:
    return local_data(ep, "transactions")

def ledger_loc(ep: int, ledger_hash: str) -> pathlib.Path:
    return local_data(ep, ledger_hash)
