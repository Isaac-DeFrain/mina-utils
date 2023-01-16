# voting-results

## setup

Check `python3` version >= 3.7

```sh
python3 --version
```

Clone the repo

```sh
git clone git@github.com:Isaac-DeFrain/mina-utils.git
```

Navigate to `voting-results`

```sh
cd mina-utils/scripts/voting-results
```

## calculate voting results

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

## Test

Run the unit tests

```sh
pytest
```

## MIP1 results

```sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~ Voting Results Report ~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keyword: mip1

>>> Totals
Num epoch txns: 56838
Num yes votes:  66
Num no votes:   4
Vote stake:     227613505.41038996

>>> Weights
Yes vote weight: 0.9847764795481286
No vote weight:  0.015223520451871479

>>> Voting details
{
    "B62qnZbq4CLNGjuvyQV38AHAZsLmid2Xy9KBQuo8hVCfzGzzqkDXL4A": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qnVMHrtGPVRN3SrwyDzjbgBQhaFSgv16SAAFe5ddm2369KKzRn6d": {
        "vote": "no mip1",
        "stake": 123560.23695542799,
        "weight": 0.0005428510787734117
    },
    "B62qjrwcG6cbvartJ63wJQQxYx1aY9N1gh8fhYkG8AwDmwQY42XfG6Y": {
        "vote": "mip1",
        "stake": 2183917.2927608327,
        "weight": 0.009594849342631067
    },
    "B62qnR2AHmcnyb7v3cVvuZWriEnArx7yMkXBcnzpFQXCmGxAAv4nJSV": {
        "vote": "mip1",
        "stake": 121071.622463962,
        "weight": 0.000531917568975832
    },
    "B62qixS4sPhp5dDwGsKvz7W312iekSmzdEJc4VNpcrZACr2m7KH9qNv": {
        "vote": "mip1",
        "stake": "B62qj7tJG5rxdy1hxo2tPo8xJGN3qDHwQdPqq7UMH6xGfhyfUikyKV8",
        "weight": "N/A"
    },
    "B62qj7tJG5rxdy1hxo2tPo8xJGN3qDHwQdPqq7UMH6xGfhyfUikyKV8": {
        "vote": "mip1",
        "stake": 85766.012896518,
        "weight": 0.00037680546565934574
    },
    "B62qqKoxyhPfHY9kw283dafk5jztbbKdH78eDXpNCyj69cmckC8KZqs": {
        "vote": "mip1",
        "stake": 1060533.0586674511,
        "weight": 0.004659359104176604
    },
    "B62qjFW9CbdJERZeiJ3rZesCoVXJ9wXiB4ecN6W4d8XQ6gLKnS1Cz2A": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qjrusP6NiGW8AVXsBtHQ1rgLnwuZFhKodA6QhsJU4n8d4rgFQYy4": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qjhiEXP45KEk8Fch4FnYJQ7UMMfiR3hq9ZeMUZ8ia3MbfEteSYDg": {
        "vote": "mip1",
        "stake": 1368675.4093339536,
        "weight": 0.006013155532516469
    },
    "B62qqoKVSdGELy1tnhKjmgYBtxGYN5SHSxAYCWDiAvuF3ycuGaLQhqQ": {
        "vote": "no mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qmDvkaMuzQnGK8D31no2rKnvoCPBwqeH4VJZFgU9gNYF2ZB4GPQp": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qrae3PEBj66KV2obWnzVxMjDCMuFWnyzxEzvLkQutaKPmWtfUPm3": {
        "vote": "mip1",
        "stake": 2431945.480014706,
        "weight": 0.010684539459246403
    },
    "B62qjLbRHR1BQYKXgxWriLmbSiVCcrXBdYPWTBghV2PzAE95FzNUyjN": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qrnPdz8HpsDJfGHirDLpVrN2VeyeitdaTKBaccWtHpeVW9Hgwi75": {
        "vote": "mip1",
        "stake": 88398.38254963,
        "weight": 0.000388370551168511
    },
    "B62qjok2BD2jB6TArVM1oGDSo16xk1SYGzTwZSjx63WbtZy4BuzPBDj": {
        "vote": "mip1",
        "stake": 77952.078530734,
        "weight": 0.0003424756294235943
    },
    "B62qnTdTtkepo2yfBXCeMp9afk77oo3EKWDNWuvLzEHSZz2gkgr5JHj": {
        "vote": "no mip1",
        "stake": 2254074.987290769,
        "weight": 0.009903081028635114
    },
    "B62qpmtNBJVa3c7XAaUg8V9LnbAiXdAuJmEkSBmAcfhYsSpp9FeBQN4": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qoM9SJD7XqPKjW997sUjVA3yLfEhw1woy44CtMuZBm5HnxMPU9sc": {
        "vote": "no mip1",
        "stake": "B62qnTdTtkepo2yfBXCeMp9afk77oo3EKWDNWuvLzEHSZz2gkgr5JHj",
        "weight": "N/A"
    },
    "B62qneVkWLzKDpevT5NKR4j9H67F9m8W8SCn6w2ErHrzdtaS5W3FbvL": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qmXpWtVCSsv6Rt1fEsHaSHYyxUdo7pNWBg9DUqpMujXhCRPU4fh9": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qpqpjjzYu1tMS2aYBaCroe1KLetpBEKtnjCHLrEN35UXywino8aG": {
        "vote": "mip1",
        "stake": "B62qptf4MGw8h6tJyd7b1Bbqysfk3UVyRBEukCZEHuNSJEretDBDWYs",
        "weight": "N/A"
    },
    "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6": {
        "vote": "mip1",
        "stake": 6332902.546651632,
        "weight": 0.02782305265776444
    },
    "B62qqTrdFMmaiNerjXnBrfybAoNRSfGzsHhVEE53Fr8aMZsWcer6FC7": {
        "vote": "no mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qn7HrKKt5ia1dvGYHuvuFGLdwNSXUSAERQgvS2yZbZvVaK5biQef": {
        "vote": "mip1",
        "stake": 1022288.811977227,
        "weight": 0.004491336356048064
    },
    "B62qoVopcNoQPFydweGWUBnJJbrokkebVDiWGmAzYoaLysrFfzNCbya": {
        "vote": "mip1",
        "stake": 1181632.2213090009,
        "weight": 0.005191397668510502
    },
    "B62qid146JcZD6eSrDt2p9iqrQC6eTxRxYB5HUyg5XpTezsqP73WWRR": {
        "vote": "mip1",
        "stake": 1064301.650770035,
        "weight": 0.004675916083499027
    },
    "B62qrJfR8NpSvGJHTFm3yokiGQwczHEFKFvMSLC3R1NeuPbHSitw1ny": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qnCwc9E6dfgB3Vkc5ZZ8CxfCvaYbwvzBBF8826NMMQSdPxUsfBWp": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qjqHT76grKVpJMSEQRVtf9UeFDs8zYMRztoV42pSDc9dySSniuVN": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qj28AitWwLTU3HAhtoW34nJ6LkyHU7XKm5wC84q1RtF4ho1yEgGn": {
        "vote": "mip1",
        "stake": 2115082.8463859633,
        "weight": 0.009292431231496754
    },
    "B62qixmqCUR4GPHbbG27BpjNstYfYmfB1QwEzWVCaYs9TpSugweiVvX": {
        "vote": "mip1",
        "stake": "B62qs2Lw5WZNSjd8eHBUZXFYyRjV8oKtrZMFDn1S1Ye62G71xCQJMYM",
        "weight": "N/A"
    },
    "B62qoTCCaXTdQwiN3C1JYZkgjP4L8rKQrrrqpnGWhsSHjvSPzYVqTWR": {
        "vote": "mip1",
        "stake": "B62qs2Lw5WZNSjd8eHBUZXFYyRjV8oKtrZMFDn1S1Ye62G71xCQJMYM",
        "weight": "N/A"
    },
    "B62qp3NP4uGMRwBLBcr1JP8yzF27Wsm4QhL6yijJqo3Po1gZXWHiZxo": {
        "vote": "mip1",
        "stake": "B62qs2Lw5WZNSjd8eHBUZXFYyRjV8oKtrZMFDn1S1Ye62G71xCQJMYM",
        "weight": "N/A"
    },
    "B62qrEpQMYwujaWHNswuY3Gud5i4FLkrRwds5RNYPVyh5FwZJXgsfPV": {
        "vote": "mip1",
        "stake": "B62qs2Lw5WZNSjd8eHBUZXFYyRjV8oKtrZMFDn1S1Ye62G71xCQJMYM",
        "weight": "N/A"
    },
    "B62qnf6HwqLakFZezkKRrK2VQgeFFMTgkfsk4XCJy2CrmB5Zn5J2Y9b": {
        "vote": "mip1",
        "stake": "B62qnSjFGjZ39C8iDGMErbFSX5NvKVyvjvHxvf7U1oDmyeU6ynxXZZF",
        "weight": "N/A"
    },
    "B62qid7mcNh29WVifR2qWQDLJ9dRu94EUcbsgrTr9fdFMGsPQzWv8Qo": {
        "vote": "no mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qnbnTsbdVjXgWsYgwWY4FLzh4EqQXFWF3hxJrvcUb76J8NZNHxZQ": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qp8TJyLYVFR6FnQAZ4A3aBKCMkEZzWBo3VSuGkyhBMdFAgjhTtE9": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qr6SB6kaJAmAiRrWkFoHN9htKh2j7H7UZ3uyTGxtkMXqNqhTEZX1": {
        "vote": "mip1",
        "stake": "B62qrgnUUduZy2z7zT8qCV8ngTJfSS1rK3Wh22SHUmrse3Tfqvrhx8q",
        "weight": "N/A"
    },
    "B62qrgnUUduZy2z7zT8qCV8ngTJfSS1rK3Wh22SHUmrse3Tfqvrhx8q": {
        "vote": "mip1",
        "stake": 89508.868517595,
        "weight": 0.00039324937400445287
    },
    "B62qrJ6V72vUoqTnJUsXwBFbCU2cCk42To4mmRRY19NiGMZqJuYLLJP": {
        "vote": "mip1",
        "stake": 86651.164475008,
        "weight": 0.0003806943015915285
    },
    "B62qqDDZYhfU7mNcQKJfWHDJ3JjVTi6dG32oWiWY3KrrX4mSMLdEuUj": {
        "vote": "mip1",
        "stake": 50011.549474612,
        "weight": 0.00021972136224711518
    },
    "B62qkmeCmpn23dHJ51r5voDvqC1UqM2jDGkqw2puoyLWpDXST9gKtiu": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qinwCtxLjDmeuW3C9WFJmDpvsK2nq8ANDpDFQAQwur4DnSW3Qnu7": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qruYNPQbpXMc49cCgNbsmWahfitLeZgs3t9JnGjAjxr7RL4X51hp": {
        "vote": "mip1",
        "stake": "B62qjSytpSK7aEauBprjXDSZwc9ai4YMv9tpmXLQK14Vy941YV36rMz",
        "weight": "N/A"
    },
    "B62qj7bWVXR2mqzSLJmtwfdEnDAvuBgGkXz7aCaed3ZerqCBj9wCGVo": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qknJSP3q28HrstZ8trCWQR3DGaSWzYuNQSi1JkZxgbyuxGdp3Fw5": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qoE6byEu2xrD3ZiWzciKfpC3vAi4xR1rtViSNneovzcAMzcidbgb": {
        "vote": "mip1",
        "stake": 49.999,
        "weight": 2.1966622722958019e-07
    },
    "B62qjFhM38ZbjXqvEh4KYBX1Y4zTJJf9a3qvgPLV76VhGgHq5e2Bfgm": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qkRQ5eHDQhAN5T5TumG1gxDVcm58UhoAr45C2YwfVyTnvDpBxPJo": {
        "vote": "mip1",
        "stake": "B62qs2Lw5WZNSjd8eHBUZXFYyRjV8oKtrZMFDn1S1Ye62G71xCQJMYM",
        "weight": "N/A"
    },
    "B62qpanxZjnQLtZHQfY8VGgCYyE29aDcG7BL2KwkQJbDzaSxwwZqT7i": {
        "vote": "mip1",
        "stake": 988711.438660425,
        "weight": 0.004343817107327468
    },
    "B62qqYgjPA3VwKEnmWy7Cwp9fVPsZskTXQTKQdmw8qqKgznzarSEfXM": {
        "vote": "mip1",
        "stake": 1054670.898275397,
        "weight": 0.0046336042159440954
    },
    "B62qjwh3KGD68vYySr2V1jcpkZ9uZZSoJJHzNWCgQQiLU3DAoab5NT5": {
        "vote": "mip1",
        "stake": "B62qqYgjPA3VwKEnmWy7Cwp9fVPsZskTXQTKQdmw8qqKgznzarSEfXM",
        "weight": "N/A"
    },
    "B62qre3uW42cN528GxB41uYMMdqoow9zKgtnYb7rLm7PDvDmEEyM5ac": {
        "vote": "mip1",
        "stake": "B62qqYgjPA3VwKEnmWy7Cwp9fVPsZskTXQTKQdmw8qqKgznzarSEfXM",
        "weight": "N/A"
    },
    "B62qizsZqX5rtQa6vnkEYg5725jTH2vDkoSUSWocS1zopqQbYaNKuww": {
        "vote": "mip1",
        "stake": "B62qkDkpWabpwmJnn1Nx6tLrzusdYp1eAT89JzfYJfq95h9vzSdL9CK",
        "weight": "N/A"
    },
    "B62qmcUnts39KieV6R9MwdXKeAP8npLmkuDdivX6mnDj7ZoCsdBbn81": {
        "vote": "mip1",
        "stake": "B62qjSytpSK7aEauBprjXDSZwc9ai4YMv9tpmXLQK14Vy941YV36rMz",
        "weight": "N/A"
    },
    "B62qpPUdkUYedVERdb7XG9KLTQaQMZ5GcytqN6Ds6Z4UtJu5EJZ5xhb": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qs2Lw5WZNSjd8eHBUZXFYyRjV8oKtrZMFDn1S1Ye62G71xCQJMYM": {
        "vote": "mip1",
        "stake": 18435803.062189847,
        "weight": 0.08099608601409598
    },
    "B62qkfVPPPnG1XP3x1wuGc7Pv7usEXLKwoojv4Ybk4HTz4HRXjobWZN": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qokhrwxatVHoYNzJXy7u18fU4HQ9aWrw4NsMEUaBzozT3toVTcQK": {
        "vote": "mip1",
        "stake": "B62qpYmDbDJAyADVkJzydoz7QeZy1ZTiWeH1LSuyMxXezvu5mAQi53U",
        "weight": "N/A"
    },
    "B62qjnj5QZkbj54jMZFbLSwmDz5iddqAEH7RyzLu8gSux2f2pfv5Tzj": {
        "vote": "mip1",
        "stake": "B62qpYmDbDJAyADVkJzydoz7QeZy1ZTiWeH1LSuyMxXezvu5mAQi53U",
        "weight": "N/A"
    },
    "B62qjXjh8pMEXMs5w3CQmjLsTgxnmmrnYPYEmD7zfXNMV4yhRqmujNW": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qkEAGKnmev6yy9DEUg1S5WQ7XimLFK5yn24b4NfNMfarBry7hCKm": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qonKJKxzr2vngKZnBuzFxHw3GnC8v6fATKKJHYNJVxB2f667uBnh": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qrLAWDtLbRWFaxFb3FacvxGi2GB4GimyVrb1r1YAAja5jcJrC1xo": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qmxWNwVFVCZzQXoj8oJQ5i4ZZw1HBinBY7TtDhVjC3jeXcXEuiZj": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qnUo3EsrkznxASNsWevva9ysooi6gK8BsTeQyjvu4DJvfhurgd66": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qkPF4vCnsZ1nN2fQzJqi7YgtcXJd4nbtjsaczN6aoCAcUCLpRw1o": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qrsCqquyu7DoLTdZMzZcBCW6xqt5zvVrPP7LojtwLVEpv7SjXN2r": {
        "vote": "mip1",
        "stake": 0.3896,
        "weight": 1.7116734760424097e-09
    },
    "B62qrJnYUduaBUHht5qDjKmg1mV5SVmtDm7YNLENvdT7duvdBovTqSy": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qr9RYXVLnLa5EL8WVXJCpZsFYK1GLGk171eyeaBZhCPmKC7pYdWX": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qreLJCDr4LucfpMYjkvcoKLFsfcwrprdmoFxjt8kHebgLowDZEsQ": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC": {
        "vote": "mip1",
        "stake": 9388991.790018665,
        "weight": 0.041249713074319544
    },
    "B62qm5rhYjDq6P2uYKyjvhiSjF287quSeX1hFCd2Sv1TTfHPA4ySR5b": {
        "vote": "mip1",
        "stake": "B62qns9cPvDwckhJXHpWZZ8b8T8oUgoF4Enpax5zNVBYYMtQwHf4Cmp",
        "weight": "N/A"
    },
    "B62qrpJhFBbTXNe9UVWyf8AmDu4KPg1H3SS6FYvupkfEt515oCDi8ux": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qoKZLSQT9jJs3kAt7bXtS3tRwZVFkPkdBnvqs6jr9mVismyD7Eey": {
        "vote": "mip1",
        "stake": 2200167.950070539,
        "weight": 0.009666245182172337
    },
    "B62qmLRLxC5Fx3cRmHDwKGq6psCbmXAYE1UsS4Z1foqrXCTtJuvTbbL": {
        "vote": "mip1",
        "stake": 2262176.780214811,
        "weight": 0.009938675546233861
    },
    "B62qiYQDFkC7rejdUE8fXPEnDq5dT7oyg5yGTSeRHvMnRwXgnuYZD9c": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qr9tCR4g4p7BiyvPhazR1fuVoRquBr5obt7rVfwuRc1yLUmC4sEF": {
        "vote": "mip1",
        "stake": "B62qj28AitWwLTU3HAhtoW34nJ6LkyHU7XKm5wC84q1RtF4ho1yEgGn",
        "weight": "N/A"
    },
    "B62qnMmBCKJn1xZMKersEeu7U9pmKXy512VYjQ5cJ9GgLuHefmJppCR": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qp6qMf3Do4q4aKqEsLxVpVuXJaRCijtyhsjZBvDSEFUBGXg8Z9cs": {
        "vote": "mip1",
        "stake": 2312961.1110467706,
        "weight": 0.010161792055688757
    },
    "B62qib4T6We3KieS2p2K3SYkVdUMfkaWCiD5phyRAbBc2LgU4KYzt27": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qmq3nmAeLeiaVHD3WNt9pn2eAGWGTXWujhC4ixrkeRaQNUaYCb4h": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qkm7Tt5CUy3ZQB3YtzfzkmE31ABmDRnrEAzuyFVhdbTGWA5rgN6T": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qr41Mf7gCaRXN2dn8yBCe5D5bedQ82gyG2ELtkx5Vcd3HNcnVhxE": {
        "vote": "mip1",
        "stake": 2175971.163168168,
        "weight": 0.009559938718244619
    },
    "B62qjhHENLQeq9KCTHZWEBQU6hR36JBkHqv9BQR7TDeWN4a5qxuoHoD": {
        "vote": "mip1",
        "stake": 181.602743604,
        "weight": 7.978557479555883e-07
    },
    "B62qjFstxvS3pdTkLftrQkEJstcpkqNoUvSbS2ztrjHrtRoFftbLZQ6": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qp15KCww8HMrQBtGCyNf6aRdKCFvnEeNDLrLjjhGmALrV2md3VVg": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qotH4cX1ETbjNxzERWcWRzjRayAApUGAzobbN5XsmdsLK88CwZBt": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qkXfUAJknvcwT6nEwgLD79ZZd896PYHcAYN2YewSYLS4jFbaGQke": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qjhjSCEtcYevxe3eCK6gCnCt3ciYXAxtB3MZ64qZAnMR7DFA8nLk": {
        "vote": "mip1",
        "stake": "B62qqV16g8s744GHM6Dph1uhW4fggYwyvtDnVSoRUyYqNvTir3Rqqzx",
        "weight": "N/A"
    },
    "B62qrQVEMzZSpnfZsDoTXtFNPcbrAogL22TS7pLam6Ex9sDNAG6pCYj": {
        "vote": "mip1",
        "stake": "B62qqV16g8s744GHM6Dph1uhW4fggYwyvtDnVSoRUyYqNvTir3Rqqzx",
        "weight": "N/A"
    },
    "B62qjfyVSMmLfjvR8iv5Z74B4sToQfoeUgbHSYN23yRVsgJBWtV1yRv": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qqy1biWtfh6MZr8ytzgWfJ5E4j7haH6p6xn8CPriKMEjtGcQBKQ8": {
        "vote": "no mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qnd1rPUp4aBpjVjCJ3XLXk64WxuM9ff3UkfZoRCkBF8vcyFnXNTs": {
        "vote": "mip1",
        "stake": 983141.9688977959,
        "weight": 0.004319348129739397
    },
    "B62qpvyQxKG2gzVRcV433KsC1ieJqW1ao7NGrQAnswVxknTWJUhPphp": {
        "vote": "mip1",
        "stake": "B62qjCuPisQjLW7YkB22BR9KieSmUZTyApftqxsAuB3U21r3vj1YnaG",
        "weight": "N/A"
    },
    "B62qnXy1f75qq8c6HS2Am88Gk6UyvTHK3iSYh4Hb3nD6DS2eS6wZ4or": {
        "vote": "mip1",
        "stake": 72982.649388449,
        "weight": 0.0003206428777451513
    },
    "B62qp69bsgUNySCY2wEYDCrRN3gdMB6cDSZGBucTzc9vUUH4jUoDSED": {
        "vote": "mip1",
        "stake": 3.232941,
        "weight": 1.4203643119378911e-08
    },
    "B62qiVQduMR4ZNaCiVGmeRnHn1V9Ju5CGsS4Rg9HvvADcRYch2Zy2y7": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qmDdMwKoMNLHZYqf3c6SJ34FmtP5HpTtFGtbDQGJrDb7cc1HtuYT": {
        "vote": "mip1",
        "stake": 2102170.751030251,
        "weight": 0.009235703071485196
    },
    "B62qkAAgs5NMapBmqmqQujhxe4jFm4ahNN5tCm6Sxqma5PTwJh9faX1": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qnRazexGJ5cwBM8ACDr994Gg6yhxEEVuZgQJ9vLWbnHQn9vLxbAM": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qoXHaQffg98Xn1mm1VtC8USicTjWDBp8xE57V2vk3ZSbPMCQSQGb": {
        "vote": "mip1",
        "stake": "B62qoazqR1ag2hDwjkSSm6qV3eJtkiPvVPKhfVyeea7TehBAWu4dWJ5",
        "weight": "N/A"
    },
    "B62qs1rLDKzuJTM9gUhdxNaCGdnGrBqGSvJ41oL3QypfbyykzC6hWur": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qiqKLsJ78CT8wTBz1r1y3F3rbDohSH6ckXUVpXr4KPAYLAyEVhue": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qkffsMQiA6e21eTaRQnpHQc63Pzp2AMLbcepyKvsC3ETSiMchTaF": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qmABHHVAiWt1F379vkdB3LHWEQYWthDwpXczYkjyXunqj6F6YABC": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qqCKwzXA6mAbyPaTSJEgLXbXkL9CZMoBsLtdsYXoPuHpRBzcoLWY": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qnDqPcQi2yULVAeK21Xk1xr8pHsq3s8QM6uAFrGubCpftB5Tf3Rx": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qo1FUbpZEGBx7jvswqCAUR1nTY1ZE7BuvMAop4dPCjQVGuqsu5gG": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qoRsL78Rjqh9BvHdp6Yog4yDKxtjyyUBi3Mdgku5RzmRFtSpHDRz": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qoZjsA51o9RabgMy9uheNkGRcPjrNU9oEB852nWJJASkp1DLtBRT": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qrm3KgXbMwSsKpqzzsmg3Me4Sd3smcjsotXoXXCkCov8DkSd7zjK": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qrBxpm9QERL7Np4ARnjWnJWhqaGK4MZG5ZKCvvrZRE7koxYpPKzB": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qjTcywX9efA4nWAvZiyTEFh2u1GFfhdFCijANaH38UGP9VJr9jmy": {
        "vote": "mip1",
        "stake": "B62qmFf6UZn2sg3j8bYLGmMinzS2FHX6hDM71nFxAfMhvh4hnGBtkBD",
        "weight": "N/A"
    },
    "B62qq24gjdzBgSPwHZ8c4HnExxJMW3LEKK6SsULtkgp79pKJixxLEPf": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qj6qzoJMLKUEZwhMJacjHCMXQDeCeMWozgdpiU72WbgAmfEZMkBT": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qjPr9oMyuNo1kYDmh98BHGcoqBDGKsrpWk53qAjbfFtKYjz6iTxs": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qp8abM9hfqzmDpJUPAhT9UiQLhEdgcGnKoBsVnKuq7QrDWPxEEpa": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qjVzvE8eDJWHVEngtvJZAb7xWq5hVyj3eXM95bDYCwVR6sRUZNe6": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qqrMZnQ81d1icj6T74q92hLpuDuBkp99eHtP4SAhD9i6RcmKeW7C": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qibLC2QVRKjAvNa3GhtN4TMmehbgJwhMuQsgwcdAGiYESKc4Wvtm": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qikFQDRv3SxgZfXP5wabQ446EQukSb1iCga56EENr2FczmUbVeG4": {
        "vote": "no mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qqrHGT2vQewqYgoBwGyunwwHoztjXjeN1JNST4vXthKYwAdvXSyX": {
        "vote": "mip1",
        "stake": 3.9989,
        "weight": 1.7568816897705318e-08
    },
    "B62qj2AqXEq6hdzaiFQ7wNSQ9TrzHQKS5WRnodXvdM7w1pRDc4GsgMV": {
        "vote": "mip1",
        "stake": "B62qjQ3k78nzaePyXhg298UEVnwbCeqQUcNwZRSR4VK1gVJ6mer6M8V",
        "weight": "N/A"
    },
    "B62qjTanvKuhcGC3vY9H4SaMsn6m5e1PGf7td7UAXZbRzVsmiB9oM8E": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qnwA5ZbknTvsQJbFarrFV9kgNp8SfZ7VdqKfikt2Lq5P6sCUc3mh": {
        "vote": "mip1",
        "stake": "B62qpYmDbDJAyADVkJzydoz7QeZy1ZTiWeH1LSuyMxXezvu5mAQi53U",
        "weight": "N/A"
    },
    "B62qohxpUiWyLKBdhzEPc9f8EoPFh2Ms1Rwp2Sp7sUShocpwGAEFu4q": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qospDjUj43x2yMKiNehojWWRUsE1wpdUDVpfxH8V3n5Y1QgJKFfw": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qj8Ld7mfYLuVramqiG9UWVjeLp5gsNy3pRCc5eF1heDMzkciNpF3": {
        "vote": "no mip1",
        "stake": "B62qrzoBfFuUxJg2YvcBkBnziVtAPziP5uAPcCPpQZgtjE4LTxXvVSJ",
        "weight": "N/A"
    },
    "B62qrVYJdL8ne3zTVtBVXPUXaWRtYC1yemy9X8j1gV9LxWn2k9nPoqj": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qpXuwSUQhfYfiu3CrZLXGzrCrxzkMNQAUZTu1bmxn8rsGH9zv7aQ": {
        "vote": "no mip1",
        "stake": "B62qrzoBfFuUxJg2YvcBkBnziVtAPziP5uAPcCPpQZgtjE4LTxXvVSJ",
        "weight": "N/A"
    },
    "B62qnrCSHAzy4pK258Bspu3ZSPjTAMjazSfZMA4uxYjJQJTAKbptuQu": {
        "vote": "no mip1",
        "stake": "B62qrzoBfFuUxJg2YvcBkBnziVtAPziP5uAPcCPpQZgtjE4LTxXvVSJ",
        "weight": "N/A"
    },
    "B62qp2KGqUdFpfNM6gY3C8ZUFrqZvCXHPwCwGujPXQGVBagFdFwR59x": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qoFYZDYiEixy91BfvM2wurrNLCPfRLAg4ufbSUrG7PwNaZYKsYs6": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6": {
        "vote": "mip1",
        "stake": 22222699.642316982,
        "weight": 0.09763348445536736
    },
    "B62qn2Ne2JGRdbHXdfD8wkA6PTWuBjaxUDQ6QuPAmggrcYjTP3HwWkF": {
        "vote": "mip1",
        "stake": 67808.080028607,
        "weight": 0.00029790886048852066
    },
    "B62qnvyPyVq9MzKzfDvCz6CWootRZjedeLog3uMrJMbFQBCYZj5ww3A": {
        "vote": "mip1",
        "stake": 0.0,
        "weight": 0.0
    },
    "B62qjsjrafURBvewWyXQLRL4to2twtXyvY1LkBgWMTFzNwF5maRmtxG": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qm6LsmCzE2v7kejoe6pBxRKheNoCkznVUQyeLqAU5xtMmKoyNf7p": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qr1TH4Yc6Bfzp9Cp8YfN3VEXNDmM8FSSQgP3nGzdSK5UVKrL7CpP": {
        "vote": "no mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qqx8uE9n7kMhCPQ71GgXNi3Dennx1hBrJXy7sr5j9TrAbV168uc9": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qqkkHiZBewA4R417fKmS3RjehKszHLWQeMbB82FC1mzaQC8Ug8eN": {
        "vote": "mip1",
        "stake": "B62qqV16g8s744GHM6Dph1uhW4fggYwyvtDnVSoRUyYqNvTir3Rqqzx",
        "weight": "N/A"
    },
    "B62qmy5TJoCCbwqXSMQGUbCktSung1CcUWn8nLjjMAQNyNH7CtijrAE": {
        "vote": "mip1",
        "stake": "B62qqV16g8s744GHM6Dph1uhW4fggYwyvtDnVSoRUyYqNvTir3Rqqzx",
        "weight": "N/A"
    },
    "B62qjL2UtdqaekzYDLjhYm7GdxzKpL7P2GwgaL2MRjZfuFaU9G5JVrb": {
        "vote": "mip1",
        "stake": 0.9899,
        "weight": 4.349038947470178e-09
    },
    "B62qijDC2gCTtcqYGnUAc9YgH2Uw4fzr8xEKKL4faZmWyAypgEe3oWC": {
        "vote": "mip1",
        "stake": 13986521.358209517,
        "weight": 0.061448556547607516
    },
    "B62qksN97EtNvQGzH2RAgnDR8zLAawhPNE1QzWCgPRcknyL6NJ3CCgJ": {
        "vote": "mip1",
        "stake": 158992.988086126,
        "weight": 0.0006985217674120859
    },
    "B62qpYmDbDJAyADVkJzydoz7QeZy1ZTiWeH1LSuyMxXezvu5mAQi53U": {
        "vote": "mip1",
        "stake": 11367197.01635861,
        "weight": 0.04994078447086615
    },
    "B62qkc27BV8cWmYM9UhEpPQnoq1XAbHSPAGNu5o1Mg1dDUgMTEReEZ3": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qo5B8mmiS9tsQygVah3mNJ8QQG3QYxboRwbA4Ky7PxJpsvAskRpM": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qoqAVGMuBrHehFWezwku1rbuAgSYrRQaFNtP7gLnd57iWqB2RgF7": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qjfS1BXRkSrHbRG7TquKZ3WBDrzXUVdmcHA3Q8iFsiFa3QFpgPhh": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qiyw8mozcCxnfzrwjp8tyZCLqQxRebK3q1D5f9NmZJ4XAYW375xz": {
        "vote": "mip1",
        "stake": "B62qkE36gg6NsvtC9EYBHDKqay1rvvPrcHq5yzRTxJUj9TJiKFcJhx2",
        "weight": "N/A"
    },
    "B62qkYYCwXyAwvC59XhxkStaxjHELkVawfso6GYh26dSpLsBGdy8mCm": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpDR99MxbrKqbpsHKJmpAdu9SvuCA6Gy6AWQoG65QXNjDoCvgTfz": {
        "vote": "mip1",
        "stake": 0.077,
        "weight": 3.3829275578866925e-10
    },
    "B62qmorGzq9SojV7mo13N3bG85iHb5NfaRZ3WJMweW5X5xDiZSnWSbJ": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qoLryvKQFWCpCCDe8NELSY79jjq4ycWfcq39fc9yVdhiiJWQF4W2": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qojSuwh8iFEbGtiktr4T1vHvybMkCBgu6Goyu1bSZCS2KQMx79RV": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qmssQTxPTUArtPVfuUqmoEzVha3ocg6wYQ8RTEV1f5uNVjDckWfk": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qkfr1Rsph7kpoveZkGpw4NQHGHgMDCZjTiFCxAVSAzM6R2fXrxQs": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qmZfqkrn4p7xeqsZiA93e4duWEDV45yLgxpMj5ZaqLzFnMno9E7e": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qpLST3UC1rpVT6SHfB7wqW2iQgiopFAGfrcovPgLjgfpDUN2LLeg": {
        "vote": "mip1",
        "stake": 990476.033826178,
        "weight": 0.004351569701632324
    },
    "B62qoXQhp63oNsLSN9Dy7wcF3PzLmdBnnin2rTnNWLbpgF7diABciU6": {
        "vote": "mip1",
        "stake": 1017372.312023841,
        "weight": 0.00446973614412513
    },
    "B62qkiF5CTjeiuV1HSx4SpEytjiCptApsvmjiHHqkb1xpAgVuZTtR14": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qs2P91UjdhngetBJ57C56HQ8t5V7ECAYWBvpkaC45ovXNgnzqfG6": {
        "vote": "mip1",
        "stake": 3628697.3414405626,
        "weight": 0.01594236394232397
    },
    "B62qpsHkfSA5Nu6tT79Bwm2N6UCwKh7ZKCmCc9j3JghuNyrYELmN8dB": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qqV16g8s744GHM6Dph1uhW4fggYwyvtDnVSoRUyYqNvTir3Rqqzx": {
        "vote": "mip1",
        "stake": 26368732.406707842,
        "weight": 0.11584871626648292
    },
    "B62qm8gXiEozEg8LggpTedU7qpreyZoMaciiqLGVXECnuWsDfoF3UDg": {
        "vote": "mip1",
        "stake": 982598.420503462,
        "weight": 0.0043169600974767505
    },
    "B62qqpujuZ5W9uGtEwJv9R9yP8475hjFd93D4fVXoVPi9tmAMsQZBhn": {
        "vote": "mip1",
        "stake": 2197439.114063051,
        "weight": 0.009654256280184435
    },
    "B62qqSDsgPh4c6E4DQw1Rbo1dCtZJMivQtXTDJcL58m95pydVupDDRE": {
        "vote": "mip1",
        "stake": 2222942.9684774023,
        "weight": 0.009766305230743707
    },
    "B62qnSjFGjZ39C8iDGMErbFSX5NvKVyvjvHxvf7U1oDmyeU6ynxXZZF": {
        "vote": "mip1",
        "stake": 6249313.566836104,
        "weight": 0.027455811796266282
    },
    "B62qqoFpNRQbrFwa2Wu5icQ8jBCe9jM4UhTM3dykp4dEGQZ9scGnA9n": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qqCmMj2mjjVuzAiZkpmVMmAPVNDwFhCVr72BGP3iPUuAsaZxJ9Zt": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qnPAkKpsQhn6S4MbefoP4Xpk8Q2yavMCa1QVvu9RveHmD2zcJxfB": {
        "vote": "mip1",
        "stake": "B62qpsikYYhTaAXw8XdgGhQtLsnecHF89LZdW2bGTa4aj4mePWPHxPe",
        "weight": "N/A"
    },
    "B62qnYBehkVZzgJBCC5yhFyF2L7mMRPsVnKW2xpcWFVuQYRVgoqwDCS": {
        "vote": "mip1",
        "stake": 2344973.309133775,
        "weight": 0.01030243484412649
    },
    "B62qmGaHwjPmQgsNRn1nazJwgBkCSgTnhAFvVEToBXButeiFayjB5LR": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qmVohHxFPyF6WF5tnc6uvSBvJ2fbn79N8kRzM7DwGwp4zNtuxRk9": {
        "vote": "mip1",
        "stake": "B62qphpEdBwSycpN67XFjcXSEY9j18chmttFTXYerhTPMX4JkXubWkd",
        "weight": "N/A"
    },
    "B62qqDXLTDLkqmW3xDiYrSCdVCdcLug52yZEFFrvVbbYCbJ4bjKazzr": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qphpEdBwSycpN67XFjcXSEY9j18chmttFTXYerhTPMX4JkXubWkd": {
        "vote": "mip1",
        "stake": 1074329.833665684,
        "weight": 0.004719974026710999
    },
    "B62qrJb5c4yaeL5fDCrEU5tGsmJWbcfnkdW1pMQbGT1rAnnA2JjAP6h": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpZyu6v99yrgsFQNKmkS3tj1m4A7sFeVo4dfjZMBNqBeXWzhvedm": {
        "vote": "mip1",
        "stake": "B62qrae3PEBj66KV2obWnzVxMjDCMuFWnyzxEzvLkQutaKPmWtfUPm3",
        "weight": "N/A"
    },
    "B62qodLP9rJBJbaMfxfph2gMoyN1vaBTKciFGzA37TyauATRrUckmdM": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qkoS4WmwwZXQyiNhyKCuKhzvcbwgwcca9aYQDdzCoAyWgZqxSjze": {
        "vote": "mip1",
        "stake": 2.7528,
        "weight": 1.209418569006557e-08
    },
    "B62qnzFxXFAq7E6RiYWiV3593uN626xmV9LQ4Pmks4tGUb8sye54Ef2": {
        "vote": "mip1",
        "stake": "B62qqSDsgPh4c6E4DQw1Rbo1dCtZJMivQtXTDJcL58m95pydVupDDRE",
        "weight": "N/A"
    },
    "B62qqakzRUUn3tuJf3u8Y2e7ubhTtuzgYBfRJSMrJmTKA7D1hxiFGJp": {
        "vote": "mip1",
        "stake": "B62qphpEdBwSycpN67XFjcXSEY9j18chmttFTXYerhTPMX4JkXubWkd",
        "weight": "N/A"
    },
    "B62qkzGbpbSM7h8onhaJ1mzJgNL4Rj25tpkBjm5MLcUy9YEWWc29SBp": {
        "vote": "mip1",
        "stake": "B62qqudRvUwyMqRy1hz2A6yuxZuKqfQE9JjxfBLxEKqSvQEobDJnBp6",
        "weight": "N/A"
    },
    "B62qmybys2vViMnedZSheEZ6ZSBjNwXHr9uBDy8kMUEJx8UsJ53r11D": {
        "vote": "mip1",
        "stake": "B62qphpEdBwSycpN67XFjcXSEY9j18chmttFTXYerhTPMX4JkXubWkd",
        "weight": "N/A"
    },
    "B62qmM9KDeqvu3TVpQStGJARgg7KppxE8UF3xMdtKV9TDc33kSUGug5": {
        "vote": "mip1",
        "stake": 2370371.530222545,
        "weight": 0.010414019703921943
    },
    "B62qqdbzp94zNRh6zhNCsiBXK2PWWSwpPfaKmdHMb4Khzj6cabEWNQj": {
        "vote": "mip1",
        "stake": "B62qjCuPisQjLW7YkB22BR9KieSmUZTyApftqxsAuB3U21r3vj1YnaG",
        "weight": "N/A"
    },
    "B62qjKzF2PDsFHRCBzgLHiTDBcvbuDcbZb3YhRyEExWixRuEXauYVLf": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qiksZ9WSGYb1pg3AvgzoQwqQy62F4pao1X2BNfj8hJFjovnh28Cw": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qih879Rtt1jGkCLii9EmP5wMdV9nJpqVpV5K2QJe3iCvrPhFKxst": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qkg6DeBGiEvfnYmxSj8JprZF1Pwzme3No4jfRMdV5RihUY26B9e2": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qjBmrdByznkZkmRUFTtMgvtXSLkB2AvRsyjfc4upjVs1NMGqaSK6": {
        "vote": "no mip1",
        "stake": "B62qpsikYYhTaAXw8XdgGhQtLsnecHF89LZdW2bGTa4aj4mePWPHxPe",
        "weight": "N/A"
    },
    "B62qmtWveRT6T8kufEvhfJbd97hw4SFz5d3nDCZdDgsQqUyWEN1VGJp": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qkCLxjMAUEaYbatpEvrGGPdUgdtR8FtdPEXYKjfwQQ4iYPrh53Yn": {
        "vote": "no mip1",
        "stake": "B62qrHzjcZbYSsrcXVgGko7go1DzSEBfdQGPon5X4LEGExtNJZA4ECj",
        "weight": "N/A"
    },
    "B62qo4tJ3EvMtQh3JPgtCfCzVdCLQpHnf2SyqJDhZ4wsL8aHdXzeYy7": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN": {
        "vote": "mip1",
        "stake": 49350863.83483965,
        "weight": 0.2168186977563543
    },
    "B62qpCAyk2N2Jxr2tYWwRDWwK25fDZWzSjKVgWfxKNzjageB97S4azD": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpokn65aEEsoXh64UubX3W8RZPCevsaxmfED3SC5KbGtLUTMdLnz": {
        "vote": "mip1",
        "stake": "B62qpYmDbDJAyADVkJzydoz7QeZy1ZTiWeH1LSuyMxXezvu5mAQi53U",
        "weight": "N/A"
    },
    "B62qpN33v3nQFPWhzwgozf4ZoX6R47FjiqT3L7hePrpuzNJXvv3em9X": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qogZXeoJsH8cYNvza55KTAMgS4AwxY2wKMUrQm8KZGCMjEaQTUoW": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qqF2kUvSDw9r4XdukwST3qtqXE1S5oVfMidV4JBr3BFHpGQ3Pd4d": {
        "vote": "mip1",
        "stake": 1091749.635148091,
        "weight": 0.004796506398773012
    },
    "B62qmP5ynbrHe1XEGD62MJB6Ahpw1qoynGaPNXjKwd6TB9Lc5d1NNPk": {
        "vote": "mip1",
        "stake": "B62qif7HxYzQCb8v2FN3KgZkS8oevDG2zqYqzkdjSV1Smf6jbEcPVEc",
        "weight": "N/A"
    },
    "B62qoePZR2pWJCHmUGsXmA5742W6ytwYeh2M81CxfuYxdCWpQvyxkPQ": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qpZQ7xcNpv6zcY75D2y1V4K1DHXVpkbCJAYpPNHgutXAb6o5QSZE": {
        "vote": "no mip1",
        "stake": 1087441.611491034,
        "weight": 0.00477757947416329
    },
    "B62qigmBqsZRoH4DYobEbYCCzuafo4V2gsytxX2wVL27isMvp4ViB4e": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qkBqSkXgkirtU3n8HJ9YgwHh3vUD6kGJ5ZRkQYGNPeL5xYL2tL1L": {
        "vote": "mip1",
        "stake": 2689796.963342801,
        "weight": 0.011817387366769226
    },
    "B62qpjGDv1phWxbMDFp5PBfoPMfUhLjQa2afbdif6QW28992RXr8UfG": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qpushwxsMN4QCBAJGJ8v7vXgE9mevGY3ZS6d6KLwWAzVwkhhRveJ": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpGgX3Dh7ih38xfCdkRrYxMbKkoVSw8UkpQh2NPZiwqhK3u84CUV": {
        "vote": "mip1",
        "stake": 25509.0,
        "weight": 0.000112071557239132
    },
    "B62qrr4HsyQDc8BHf875XHizovkMqfXYKFxqxdcLPNahHnz1GZqCmXL": {
        "vote": "mip1",
        "stake": 82123.32726355601,
        "weight": 0.0003608016453834171
    },
    "B62qobgsYd4eXNiayoEUjDox1LtJW4K5xtNZ8fawTsuxzufaL7ypM26": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qkV2PxfmyAc1ExHX2s9cTdGwVwn1Cd8jg5w7uMzqQrbxszZ4CvYc": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qpaY38GFqhUcLdA1c5EMv46xwWBxgdWM2ddEM5guH6bi81SHXFJK": {
        "vote": "mip1",
        "stake": 5832.99967458,
        "weight": 2.562677317439064e-05
    },
    "B62qpMcYjgezccPk8NfaSto4jyV3uGU8R24D9uSShMoqr8JdpAv4RKo": {
        "vote": "mip1",
        "stake": 2249296.042308708,
        "weight": 0.00988208515243065
    },
    "B62qjoVHQFKkz92h7ojYY6ZKnqzrzuPZRPwPWiUwY2d2ugNGY3YToC7": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qnR6HKx34NCyDkSeRcJ44KATjUCs4xmQYDbwTXPJPQ4J6ebfeQe4": {
        "vote": "mip1",
        "stake": 2681269.4110452384,
        "weight": 0.011779922312653972
    },
    "B62qmuLVSBTv9iH78NseE3WULSrEXAVGRWy5oGJxbMEBdUiSU9YSnH1": {
        "vote": "mip1",
        "stake": "B62qpXqPzauUXLnsAQFnYHMCiV9pRqG2wqbJ4pL936SVANHa66zkkQj",
        "weight": "N/A"
    },
    "B62qqch9XkiTS8BLUDSM1sayfXNAtnYnQFChktYG1bfCJkDMUqs98Xr": {
        "vote": "mip1",
        "stake": 2573600.5100999535,
        "weight": 0.011306888426764132
    },
    "B62qkNQGcXX789Hh5eez6fpQYZBpTooBZdh9Gn93ENgYpqbwr1EHbZw": {
        "vote": "mip1",
        "stake": "B62qjSytpSK7aEauBprjXDSZwc9ai4YMv9tpmXLQK14Vy941YV36rMz",
        "weight": "N/A"
    },
    "B62qiqpmRsgfn9ks29mjz5eqTmhi9nKGxTTgyjKn2MeThfAGgGSA1DN": {
        "vote": "no mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qqB453GCVWrkiizknzQ2oFPbGocRfSUBhsAtY6vopFohV4iAfkwe": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qjKpQPdRMXSB1fcLSTzaTqSeACjUXuzpMdHCkJ1zbhS732tCMcRA": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qppkd3QVjGNMHbSnEDRwBje2VkjpM7LeLi2N1UhwjxJTDFrTGLH5": {
        "vote": "mip1",
        "stake": "B62qrQiw9JhUumq457sMxicgQ94Z1WD9JChzJu19kBE8Szb5T8tcUAC",
        "weight": "N/A"
    },
    "B62qmzMYeNZ72s7TupkiXutV2Sf6dmniy5SBXijG9awZjpdnWszMEye": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qnZ2xvSKaP7aKFvUewJVHfiG3Mkf5nBzUD9MVWTCERszPCSJ4AR5": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpEeZEPdRrBsWEN3jK2cxeUVVX3JP6zqxwSBNKg8wjX4oMFoUVdb": {
        "vote": "mip1",
        "stake": "B62qs2Lw5WZNSjd8eHBUZXFYyRjV8oKtrZMFDn1S1Ye62G71xCQJMYM",
        "weight": "N/A"
    },
    "B62qnycGEAjHCk6jgkaqvJadY1v8gZ3FHFrDVGbxoguFG5hBgSWTm3F": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qmx5PCYWLFJRfehJ14zPWu8dtaccFVi2oUDFbDcfP4mmNgNG4xbW": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qm5ohHFmyT2QFUZ8SCDYydDvvGaZczfA8yW5cRaw5BQUe1u23MmS": {
        "vote": "no mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qqNUt1QBC1KgCyzhKr1Q95wkEvZXWEnSH4CLvUSHZC7XEM7RtDuK": {
        "vote": "no mip1",
        "stake": 2.019,
        "weight": 8.87029966152368e-09
    },
    "B62qr9jmNyuKG9Zhi1jENgPuswFRRDrkin3tP6D76qx8HNpjke5aUMs": {
        "vote": "mip1",
        "stake": 1055335.7978970928,
        "weight": 0.0046365253941953455
    },
    "B62qkqqzMpLeDEQDzfWmxDzzAkVMCt63V1RMwT9LJiyuwaBtvrSP8xV": {
        "vote": "mip1",
        "stake": "B62qpXqPzauUXLnsAQFnYHMCiV9pRqG2wqbJ4pL936SVANHa66zkkQj",
        "weight": "N/A"
    },
    "B62qk2qmsBc9iepGxrSW1NQk2RYN8SZXArqhpP9kZ1EV4Ym8u8asz5R": {
        "vote": "mip1",
        "stake": "B62qr9jmNyuKG9Zhi1jENgPuswFRRDrkin3tP6D76qx8HNpjke5aUMs",
        "weight": "N/A"
    },
    "B62qqD9f8CGy5QeFj1h3nsit3Zp2GDBntjEoVCdfj4SPQuubRW1CYXp": {
        "vote": "mip1",
        "stake": 2132607.610715391,
        "weight": 0.009369424748633757
    },
    "B62qkLxz5XqTJuUgJ2syjruQJMmNhYe2kM673Vg4LdHd9PXC1zfX3Zh": {
        "vote": "no mip1",
        "stake": "B62qix9vooX5NqJYo8nT6xWqCeQu5AJoS1ng6FRnUpVAra6PAZZ1CU4",
        "weight": "N/A"
    },
    "B62qopEsHhqoUrzu2XWjfr9HUrREraH2eRfNzZvHocPxRtMKKnjdAFi": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qrQCaKV2Y86FTSpz7U2845tLQbjCLNXKguDxbU7kpXMhTvCgMU8T": {
        "vote": "no mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qnnsamTzcyrSLXr8DvyXJ7xGrjymWbdsQUk6zNp5ctLTpjCFWER4": {
        "vote": "no mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qpZTtpZL7QobzPX97h1f2CNFchXoXc4NJUZL1xdvNqTdwR5NCbkZ": {
        "vote": "mip1",
        "stake": 383864.03326558496,
        "weight": 0.0016864730085917941
    },
    "B62qisd1ZBWPazyvjHNQptLEitZXydezfkVVRoYANF8qYWid5cg5FPB": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpv3ry6VG9XU7Lyz6hFr44h33RtQo8wsAf4fr1DdhwxiLvU8ZN4y": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qpZGfxVhvbkM6A9JnCvysUNSGJVU6DhFmFkLxxtxZZ421Gi9ztT2": {
        "vote": "mip1",
        "stake": "B62qq3TQ8AP7MFYPVtMx5tZGF3kWLJukfwG1A1RGvaBW1jfTPTkDBW6",
        "weight": "N/A"
    },
    "B62qoazqR1ag2hDwjkSSm6qV3eJtkiPvVPKhfVyeea7TehBAWu4dWJ5": {
        "vote": "mip1",
        "stake": 248872.77469357505,
        "weight": 0.0010934007375566505
    },
    "B62qpU86FVydfLiAtsS8RgRhwnQfXFaKjvTmyhbaUTBkA7Q2mcPKyn1": {
        "vote": "mip1",
        "stake": "B62qre3erTHfzQckNuibViWQGyyKwZseztqrjPZBv6SQF384Rg6ESAy",
        "weight": "N/A"
    },
    "B62qpgZyQjoZPKnyV4526TDgGPzVGfibP4Qu7CQMUGLuZLdcpQsw6te": {
        "vote": "mip1",
        "stake": "B62qq6ZYPG5JsjZnGJ3pADmRn6hU6qy13EhraTSymjSgyEDwoDR9Gd6",
        "weight": "N/A"
    },
    "B62qoc7LgaNBKgZCazrTjYpUx6YsSr6s3yQqzR7BR39gXWZhgEZa5Zw": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qmcQmcoGR9UfziQH1PnSbM23jy1Q8Xr1jKTpxJjQsjR5fJ3Dfyft": {
        "vote": "mip1",
        "stake": "B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN",
        "weight": "N/A"
    },
    "B62qp6HmxzW5XXwCMiyZiJREoJ4b7omkNuCJiThVLNM1P3u1s1a3qzp": {
        "vote": "mip1",
        "stake": 988607.0908336269,
        "weight": 0.00434335866428996
    }
}
```
