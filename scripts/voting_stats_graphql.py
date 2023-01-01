import json
import requests
import voting_stats_constants as vsc

def pp(resp: dict):
	print(json.dumps(resp, indent=4))

def template_request(query: str, variables: dict = {}) -> dict:
    '''
    Template GraphQL request
    '''
    query = " ".join(query.split())
    payload = {"query": query}
    if variables:
        payload = {**payload, "variables": variables}
    headers = {"Accept": "application/json"}
    response = requests.post(vsc.MINA_EXPLORER, json=payload, headers=headers)
    resp_json = response.json()
    if response.status_code == 200 and "errors" not in resp_json:
        return resp_json
    else:
        print(response.text)
        raise Exception(f"Query failed -- returned code {response.status_code} from {query}")

def get_ledger_hash(epoch: int) -> dict:
    '''
    Returns ledger hash for supplied epoch
    '''
    query = """query ($epoch: Int) {
  blocks(query: {canonical: true, protocolState: {consensusState: {epoch: $epoch}}}, limit: 1) {
    protocolState {
      consensusState {
        stakingEpochData {
          ledger {
            hash
          }
        }
        epoch
      }
    }
  }
}"""
    return template_request(query, {"epoch": epoch})

def get_blocks(variables) -> dict:
    """
    Returns blocks within specified parameters

    Variables: `creator`, `epoch`, `min_block_height`, `max_block_height`, `min_date_time`, `max_date_time`
    """
    query = """query($creator: String, $epoch: Int, $min_block_height: Int, $max_block_height: Int, $min_date_time: DateTime, $max_date_time: DateTime) {
  blocks(query: {creator: $creator, protocolState: {consensusState: {epoch: $epoch}}, canonical: true, blockHeight_gte: $min_block_height, blockHeight_lte: $max_block_height, dateTime_gte: $min_date_time, dateTime_lte: $max_date_time}, sortBy: DATETIME_DESC, limit: 10) {
    blockHeight
    canonical
    creator
    dateTime
    txFees
    snarkFees
    receivedTime
    stateHash
    stateHashField
    protocolState {
      consensusState {
        blockHeight
        epoch
        slotSinceGenesis
      }
    }
    transactions {
      coinbase
      coinbaseReceiverAccount {
        publicKey
      }
      feeTransfer {
        fee
        recipient
        type
      }
    }
  }
}
"""
    return template_request(query, variables)

def get_transactions(variables) -> dict:
    '''
    Returns transactions within specified parameters

    Variables: `source`, `receiver`, `kind`, `memo`, `min_block_height`, `max_block_height`, `min_date_time`, `max_date_time`, `limit`
    '''
    query = """query($source: String, $receiver: String, $kind: String, $memo: String, $min_block_height: Int, $max_block_height: Int, $min_date_time: DateTime, $max_date_time: DateTime, $limit: Int) {
  transactions(query: {source: {publicKey: $source}, receiver: {publicKey: $receiver}, kind: $kind, memo: $memo, canonical: true, blockHeight_gte: $min_block_height, blockHeight_lte: $max_block_height, dateTime_gte: $min_date_time, dateTime_lte: $max_date_time}, sortBy: DATETIME_DESC, limit: $limit) {
	memo
	source {
	  publicKey
	}
	receiver {
	  publicKey
	}
	kind
	dateTime
	blockHeight
	hash
	amount
  }
}"""
    return template_request(query, variables)
