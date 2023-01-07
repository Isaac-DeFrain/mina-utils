import pathlib

# voting
START_TIME = "2022-12-16T10:00:00Z" # UTC-5:00
END_TIME = "2022-12-31T06:59:59Z"   # UTC-5:00

PARENT_DIR = pathlib.Path(__file__).parent
LOCAL_DATA_DIR = PARENT_DIR / "voting-data"
'''
./voting_data
'''
AGGREGATED_STAKE = LOCAL_DATA_DIR / "aggregated-stake.json"
TRANSACTIONS = LOCAL_DATA_DIR / "transactions.json"
GITHUB_AUTH_TOKEN = PARENT_DIR / "voting_github_auth_token"

MINA_EXPLORER = "https://graphql.minaexplorer.com"
'''
Mina Explorer GraphQL endpoint
'''
