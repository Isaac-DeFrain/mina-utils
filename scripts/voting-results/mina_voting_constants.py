import pathlib

PARENT_DIR = pathlib.Path(__file__).parent
LOCAL_DATA_DIR = PARENT_DIR / "voting-data"
'''
./voting_data
'''
def aggr_stake_loc(ep: int):
    return LOCAL_DATA_DIR / f"aggregated_stake_{ep}.json"

def txns_loc(ep: int):
    return LOCAL_DATA_DIR / f"transactions_{ep}.json"

GITHUB_AUTH_TOKEN = PARENT_DIR / "voting_github_auth_token"

MINA_EXPLORER = "https://graphql.minaexplorer.com"
'''
Mina Explorer GraphQL endpoint
'''
