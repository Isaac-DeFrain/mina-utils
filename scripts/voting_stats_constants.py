import  os
import pathlib

# voting
START_TIME = "2022-12-16T15:00:00Z"
END_TIME = "2022-12-31T11:59:59Z"

# local
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'voting_service_key.json'
PARENT_DIR = pathlib.Path(__file__).parent

LOCAL_DATA_DIR = PARENT_DIR / "voting-data"
'''
./voting_data
'''

# mina explorer

DATA_ARCHIVE = pathlib.Path('https://storage.googleapis.com/mina-explorer-ledgers/')
