import os
import sys
import json
import requests
import mina_voting_constants as mvc

def pp(resp):
	return json.dumps(resp, indent=4)

def get_next_staking_ledger_granola_github(ep: int, ledger_hash: str):
    '''
    ### Requires github auth token

    Request the next staking ledger via hash from Granola's `mina-ledger` GitHub repo

    Write to local file {mvc.local_data_dir(ep) / ledger_hash}.json
    '''
    if not mvc.GITHUB_AUTH_TOKEN.exists():
        print(f"You must copy a github auth token to file {mvc.GITHUB_AUTH_TOKEN}")
        sys.exit(1)
    with mvc.GITHUB_AUTH_TOKEN.open("r", encoding="utf-8") as f:
        auth_token = f.read().strip()
        f.close()
    print(f"Fetching: Granola-Team/mina-ledger/main/mainnet/{ledger_hash}.json")
    os.system(f'curl -H "Accept: application/vnd.github.v4.raw" \
     -H "Authorization: bearer {auth_token}" \
     "{mvc.GRANOLA_LEDGER}/{ledger_hash}.json" > {mvc.ledger_loc(ep, ledger_hash)}')

def template_gql_request(query: str, variables: dict = {}, endpoint: str = mvc.MINA_EXPLORER) -> dict:
    '''
    Template GraphQL request
    '''
    query = " ".join(query.split())
    payload = {"query": query}
    if variables:
        payload = {**payload, "variables": variables}
    headers = {"Accept": "application/json"}
    response = requests.post(endpoint, json=payload, headers=headers)
    resp_json = response.json()
    if response.status_code == 200 and "errors" not in resp_json:
        return resp_json
    else:
        print(response.text)
        raise Exception(f"Query failed -- returned code {response.status_code} with response {response.text}")

def get_next_ledger_hash(epoch: int, endpoint: str = mvc.MINA_EXPLORER) -> dict:
    '''
    Returns ledger hash for supplied epoch

    Variables: `epoch`
    '''
    query = """query($epoch: Int) {
  blocks(query: {canonical: true, protocolState: {consensusState: {epoch: $epoch}}}, limit: 1) {
    protocolState {
      consensusState {
        nextEpochData {
          ledger {
            hash
          }
        }
        epoch
      }
    }
  }
}"""
    return template_gql_request(query, {"epoch": epoch}, endpoint)

def get_next_staking_ledger(ledger_hash: str, endpoint: str = mvc.MINA_EXPLORER) -> dict:
    '''
    Return the staking ledger

    Variables: `limit`, `ledgerHash`
    '''
    query = """query ($ledgerHash: String!, $limit: Int = 1000000) {
  nextstakes(query: {ledgerHash: $ledgerHash}, limit: $limit) {
    pk
    balance
    delegate
  }
}"""
    return template_gql_request(query, {"ledgerHash": ledger_hash}, endpoint)

def get_block_heights(variables, endpoint: str = mvc.MINA_EXPLORER):
    '''
    Returns the canonical block heights within specified parameters

	Variables: `min_date_time`, `max_date_time`
    '''
    query = """query($min_date_time: DateTime!, $max_date_time: DateTime!) {
  blocks(query: {canonical: true, dateTime_gte: $min_date_time, dateTime_lte: $max_date_time}, limit: 7140) {
    blockHeight
  }
}"""
    return template_gql_request(query, variables, endpoint)

def get_payments_in_block_height(variables, endpoint: str = mvc.MINA_EXPLORER):
    '''
    Returns the PAYMENT transactions in the specified block

	Variables: `block_height`, `limit`
    '''
    query = """query($block_height: Int!, $limit: Int = 1000) {
  transactions(query: {blockHeight: $block_height, canonical: true, kind: "PAYMENT"}, sortBy: DATETIME_DESC, limit: $limit) {
    blockHeight
    memo
    nonce
    receiver {
      publicKey
    }
    source {
      publicKey
    }
  }
}"""
    return template_gql_request(query, variables, endpoint)

def get_transactions(variables, endpoint: str = mvc.MINA_EXPLORER) -> dict:
    '''
    Returns transactions within specified parameters

    Variables: `source`, `receiver`, `kind`, `min_block_height`, `max_block_height`, `min_date_time`, `max_date_time`, `limit`, `block_height`
    '''
    query = """query($source: String, $receiver: String, $kind: String, $block_height: Int, $min_block_height: Int, $max_block_height: Int, $min_date_time: DateTime, $max_date_time: DateTime, $limit: Int = 1000) {
  transactions(query: {source: {publicKey: $source}, receiver: {publicKey: $receiver}, kind: $kind, memo_exists: $memo_exists, canonical: true, blockHeight_gte: $min_block_height, blockHeight_lte: $max_block_height, dateTime_gte: $min_date_time, dateTime_lte: $max_date_time}, sortBy: DATETIME_DESC, limit: $limit) {
    memo
    source {
      publicKey
    }
    receiver {
      publicKey
    }
    nonce
    kind
    dateTime
    blockHeight
    hash
    amount
  }
}"""
    return template_gql_request(query, variables, endpoint)

def get_blocks(variables, endpoint: str = mvc.MINA_EXPLORER) -> dict:
    '''
    Returns blocks within specified parameters

    Variables: `creator`, `epoch`, `min_block_height`, `max_block_height`, `min_date_time`, `max_date_time`, `limit`
    '''
    query = """query($creator: String, $epoch: Int, $min_block_height: Int, $max_block_height: Int, $min_date_time: DateTime, $max_date_time: DateTime, $limit: Int = 10) {
  blocks(query: {creator: $creator, protocolState: {consensusState: {epoch: $epoch}}, canonical: true, blockHeight_gte: $min_block_height, blockHeight_lte: $max_block_height, dateTime_gte: $min_date_time, dateTime_lte: $max_date_time}, sortBy: DATETIME_DESC, limit: $limit) {
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
}"""
    return template_gql_request(query, variables, endpoint)
