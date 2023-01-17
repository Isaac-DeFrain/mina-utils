# voting-results

## Setup

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

## Examples

#### `cftest-2` voting period

[Granola's votes dashboard](https://mina.vote/mainnet/cftest-2?start=1671202800000&end=1672488000000) and [Granola's results dashboard](https://mina.vote/mainnet/cftest-2/results?start=1671202800000&end=1672488000000&hash=jxWMPncjMY9VhwehhVKHhobvJuAhZcdx5kfUtX4V3dy9Rw9aMZA)

- epoch: 43
- keyword: cftest-2
- start: Dec 16, 2022 15:00 UTC
- end: Dec 31, 2022 12:00 UTC
- writes report and votes to stdout

```sh
python3 -m mina_voting -v \
    -ep 43 \
    -kw "cftest-2" \
    -start 2022-12-16T15:00:00Z \
    -end 2022-12-31T12:00:00Z
```

#### `mip1` voting period

[Granola's votes dashboard](https://mina.vote/mainnet/mip1?start=1672848000000&end=1673685000000) and [Granola's results dashboard](https://mina.vote/mainnet/mip1/results?start=1672848000000&end=1673685000000&hash=jxQXzUkst2L9Ma9g9YQ3kfpgB5v5Znr1vrYb1mupakc5y7T89H8)

- epoch: 44
- keyword: mip1
- start: Jan 4, 2023 16:00 UTC
- end: Jan 14, 2023 8:30 UTC
- write report file
- write votes file

```sh
python3 -m mina_voting \
    -report \
    -votes \
    -ep 44 \
    -kw mip1 \
    -start 2023-01-04T16:00:00Z \
    -end 2023-01-14T08:30:00Z
```

## Test

Run the unit tests

```sh
pytest
```
