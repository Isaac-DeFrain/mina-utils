# voting-results utils

## Setup

```sh
# Check python3 version >= 3.9
$ python3 --version

# Clone the repo
$ git clone git@github.com:Isaac-DeFrain/mina-utils.git

# Navigate to voting-results
$ cd mina-utils/scripts/voting-results
```

## How to calculate the results of voting

- Epoch number of voting period: `ep`
- Need epoch `ep + 2` *staking ledger* to calculate delegations
  - *next staking ledger* of epoch `ep + 1`

```sh
# Example voting period:
# - epoch: 44
# - keyword: mip1
# - start: Jan 4, 2023 16:00 UTC
# - end: Jan 14, 2023 8:30 UTC
# - print raw votes json to stdout
python3 -m mina_voting -ep 44 -kw mip1 -start 2023-01-04T16:00:00Z -end 2023-01-14T08:30:00Z -v
```
