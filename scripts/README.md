# Mina scripts

## [Voting](./voting-results/mina_voting.py)

```sh
# from mina-utils/scripts/voting-results
python3 -m mina_voting --help

# run unit tests
pytest
```

## Keys

Python script for generating cryptographically secure passwords, keypairs, and env file for mina

```sh
# from mina-utils/scripts
python3 -m mina_gen_keypair --help
```

## Daemon

### start

Start the daemon

```sh
# from mina-utils/scripts
sh ./mina_start.sh
```

### snark

Set the snark worker and fee for a mina node

```sh
# from mina-utils/scripts
python3 -m mina_snark --help
```

## Archive

### run

You must have a PostgreSQL db `archive` and a server listening on port `5432`

Start a mina archive node instance with `postgres` user and connect to the `archive` db with `--server-port 3086`

```sh
# from mina-utils/scripts
sh ./mina_archive_run.sh
```

### archive daemon

Start a mina daemon with `--server-port 3086`

```sh
# from mina-utils/scripts
sh ./mina_archive_daemon.sh
```

### [postgres user scripts](./postgres_scripts/)

Sets up the `postgres` user for an archive node
