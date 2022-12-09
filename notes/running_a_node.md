# [Running a node](https://docs.minaprotocol.com/node-operators/getting-started)

[CLI reference](https://docs.minaprotocol.com/node-operators/mina-cli-reference)

Clone `mina` repo

```sh
git clone https://github.com/MinaProtocol/mina
```

## Set up the `stable` package repos

```sh
echo "deb [trusted=yes] http://packages.o1test.net $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/mina.list
sudo apt-get update
sudo apt-get install -y curl unzip mina-mainnet=1.3.1.2-25388a0
```

Check it works

```sh
mina version
```

Should get something like `Commit 9b0369c27bb85c8ab2f8725c6e977eb27b53b826 on branch master`

## Set up port forwarding and allow in firewall

If you are running a firewall (you really should), you will need to allow traffic on `TCP` port `8302` (the node connects to the network using this default port). Additionally, unless the `-external-ip YOUR_IP` flag is provided, the daemon will use `403/https` and `80/http` to try and determine its own IP address.

You may need to configure your router's port forwarding to allow inbound traffic to the following ports through your external IP address

- `8302/tcp`
- Optionally to use the GraphQL service, expose `3085/tcp`

See [firewall commands](./general_linux_commands.md#firewall) for more details

## [Generate keypair](https://docs.minaprotocol.com/node-operators/generating-a-keypair)

- `mina-generate-keypair`
- [Ledger hardware wallet](https://docs.minaprotocol.com/using-mina/ledger-hardware-wallet)
- [client SDK](https://docs.minaprotocol.com/node-operators/generating-a-keypair#client-sdk)

### Install `mina-generate-keypair`

Assuming you've installed the latest `stable` package repos (see [set up the stable package repos](./running_a_node.md#set-up-the-stable-package-repos)), do

```sh
sudo apt-get install mina-generate-keypair=1.3.0-9b0369c
```

Check it works

```sh
mina generate-keypair -version
```

Should get something like `Commit 9b0369c27bb85c8ab2f8725c6e977eb27b53b826 on branch master`

### Usage

This [python script](../utils/scripts/mina_gen_keypair.py) does 1 - 4. Do

```sh
cd utils/scripts
python
```

1. Make keys dir

```sh
mkdir ~/.mina-keys
```

2. Set owner read, write, execute permissions

```sh
chmod 700 ~/.mina-keys
```

3. Generate a keypair

```sh
mina-generate-keypair --privkey-path ~/.mina-keys/<KEY_NAME>
```

4. Revoke owner execute permissions

```sh
chmod 600 ~/.mina-keys
```

## Ledger hardware wallet

[Auro wallet](https://www.aurowallet.com/)

The Auro Firefox extension does not currently support Ledger

[Clor.io wallet](https://github.com/nerdvibe/clorio-client/releases/tag/v1.0.0)

## [Connecting to Mainnet](https://docs.minaprotocol.com/node-operators/connecting-to-the-network)

Assuming you've [installed the `stable` package repos](./running_a_node.md#set-up-the-stable-package-repos) do

```sh
sudo apt-get install --yes apt-transport-https
sudo apt-get install --yes curl unzip mina-mainnet=1.3.1.2-25388a0
```

Create `.mina-env` file

If you want your node to **produce blocks** do

```sh
# write the following to ~/.mina-env
MINA_PRIVKEY_PASS="<YOUR_WALLET_PRIVKEY_PASS>"
LOG_LEVEL=Info
FILE_LOG_LEVEL=Debug
EXTRA_FLAGS=" --block-producer-key <BLOCK_PRODUCER_KEY_PATH>"
PEER_LIST_URL=https://storage.googleapis.com/mina-seed-lists/mainnet_seeds.tx
```

If you only want your node to connect to peers and **produce no blocks** do

```sh
# write the following to ~/.mina-env
PEER_LIST_URL=https://storage.googleapis.com/mina-seed-lists/mainnet_seeds.tx
```

Alternatively, you can supply the python script with `--env` or `--only-env` to generate this file

[Start](../scripts/mina_start.sh) mina node instance

```sh
systemctl --user daemon-reload
systemctl --user start mina
systemctl --user enable mina
sudo loginctl enable-linger
mina daemon --peer-list-url https://storage.googleapis.com/mina-seed-lists/mainnet_seeds.txt
```

Save mina pub key env var

```sh
export MINA_PUBLIC_KEY=<YOUR-PUBLIC-KEY>
```

Alternatively, you can supply the python script with `--pubkey` to save the env var

Confirm node is running and made connections (it may take a minute or so for the daemon to start and make connections)

```sh
mina client status
```

Should get something like

```
Mina daemon status
-----------------------------------

Global number of accounts:                     134011
Block height:                                  205369
Max observed block height:                     205369
Max observed unvalidated block height:         205369
Local uptime:                                  19m59s
Ledger Merkle root:                            jwgNo5DyGu2nPRLktG1d6L3vGqJeQJZoUNSaTzZ7vPnRa3WEwGD
Protocol state hash:                           3NLnBi3HVyXMe865Zrug5ZcbBeUMobCcaCywKMEbR8PQ1aSefNZP
Chain id:                                      5f704cc0c82e0ed70e873f0893d7e06f148524e3f0bdae2afb02e7819a0c24d1
Git SHA-1:                                     25388a0fed9695e8e9d04f75f50c2bae1c9c80db
Configuration directory:                       <PATH_TO_MINA_CONFIG>
Peers:                                         31
User_commands sent:                            0
SNARK worker:                                  None
SNARK work fee:                                100000000
Sync status:                                   Bootstrap
Catchup status:                                
	To build breadcrumb:           0
	To initial validate:           0
	Finished:                      15
	To download:                   0
	Waiting for parent to finish:  0
	To verify:                     0

Block producers running:                       0
Coinbase receiver:                             Block producer
Best tip consensus time:                       epoch=42, slot=3877
Best tip global slot (across all hard-forks):  303757
Consensus time now:                            epoch=42, slot=3877
Consensus mechanism:                           proof_of_stake
Consensus configuration:                       
	Delta:                     0
	k:                         290
	Slots per epoch:           7140
	Slot duration:             3m
	Epoch duration:            14d21h
	Chain start timestamp:     2021-03-17 00:00:00.000000Z
	Acceptable network delay:  3m

Addresses and ports:                           
	External IP:    <EXTERNAL_IP>
	Bind IP:        0.0.0.0
	Libp2p PeerID:  12D3KooWAve5312B5XbFM6UtLxLa1AM2zT2XFsgEJfpUPKrBfN7w
	Libp2p port:    8302
	Client port:    8301
```

## [Sending a payment](https://docs.minaprotocol.com/node-operators/sending-a-payment#using-a-connected-node)

Import local account

```sh
chmod 700 ~/.mina-keys
mina accounts --privkey-path ~/.mina-keys/<YOUR_WALLET_NAME>
chmod 600 ~/.mina-keys
# should get something like the following:
# 😄 Imported account!
# Public key: B62qpP7yjM4F6XFk9vgq87r8W8s8BER7RYShMnKgadWrb4Gmr58FWNL
```

Alternatively, you can supply the python script with `--import-account`

Create local account

```sh
mina accounts create
```

Check your balance(s)

```sh
mina accounts list
```

Unlock your account and make a payment

```sh
mina accounts unlock --public-key $MINA_PUBLIC_KEY
mina client send-payment \
  --amount 1.5 \
  --receiver $MINA_PUBLIC_KEY \
  --fee 0.1 \
  --sender $MINA_PUBLIC_KEY
```

### TODO [Advanced transactions](https://docs.minaprotocol.com/node-operators/sending-a-payment#advanced)

## [Staking and snarking](https://docs.minaprotocol.com/node-operators/staking-and-snarking)

**TODO no `set-staking` client subcommand**

To delegate stake do

```sh
mina account unlock --public-key $MINA_PUBLIC_KEY
mina client delegate-stake \
    --receiver <DELEGATE-PUBLIC-KEY> \
    --sender $MINA_PUBLIC_KEY \
    --fee 0.1
```

*Note*: there is a latency period of 2-4 weeks before new stake delegation goes into effect

To set snark worker do

```sh
mina client set-snark-work-fee <FEE>
mina client set-snark-worker --address $MINA_PUBLIC_KEY
```

Confirm it worked

```sh
mina client status
# the SNARK worker field should now be <MINA_PUBLIC_KEY>
```

### Using `daemon.json` to configure mina daemon

Create the file

```sh
touch ~/.mina-config/daemon.config
```

Example `daemon.json` file

```
{
  "daemon": {
    "client-port": 1000,
    "external-port": 1001,
    "rest-port": 1002,
    "block-producer-key": "/path/to/privkey-file",
    "block-producer-password": "mypassword",
    "block-producer-pubkey": "<MY PUBLICKEY>",
    "coinbase-receiver": "<MY PUBLICKEY>",
    "log-block-creation": false,
    "log-received-blocks": false,
    "log-snark-work-gossip": false,
    "log-txn-pool-gossip": false,
    "peers": ["seed-one.o1test.net", "seed-two.o1test.net"],
    "run-snark-worker": "<MY PUBLICKEY>",
    "snark-worker-fee": 10,
    "snark-worker-parallelism": 1,
    "work-reassignment-wait": 420000,
    "work-selection": "seq"
  }
}
```