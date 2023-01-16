# Mina scripts

## [Mina voting results](./voting-results/mina_voting.py)

Run `mina_voting` commands from `mina-utils/scripts/voting-results`

```sh
python3 -m mina_voting --help
```

-----

Run all remaining commands from `mina-utils/scripts` (here)

## [Mina keypair generation](./mina_gen_keypair.py)

Python script for generating cryptographically secure passwords, keypairs, and env file for mina

```sh
python3 -m mina_gen_keypair --help
```

## [Mina start](./mina_start.sh)

Start a mina node instance

```sh
sh ./mina_start.sh
```

## [Mina snark](./mina_snark.py)

Set the snark worker and fee for a mina node

```sh
python3 -m mina_snark --help
```

## [Mina archive run](./mina_archive_run.sh)

You must have a PostgreSQL db `archive` and a server listening on port `5432`

Start a mina archive node instance with `postgres` user and connect to the `archive` db with `--server-port 3086`

```sh
sh ./mina_archive_run.sh
```

## [Mina archive daemon](./mina_archive_daemon.sh)

Start a mina daemon with `--server-port 3086`

```sh
sh ./mina_archive_daemon.sh
```

## [`postgres` user scripts](./postgres_scripts/)

Sets up the `postgres` user for an archive node
