# Mina scripts

Run all commands from here (`mina-utils/scripts`)

## [Mina keypair generation](./mina_gen_keypair.py)

Python script for generating cryptographically secure passwords, keypairs, and env file for mina

```sh
$ python -m mina_gen_keypair --help
usage: mina_gen_keypair.py [-h] [--env] [--only-env] [--len LEN] [--pubkey] [--validate] [--pwd-fname PWD_FNAME] [--key-fname KEY_FNAME] [--no-produce-blocks] [--import-account]

Mina keypair generator

optional arguments:
  -h, --help            show this help message and exit
  --env                 write .mina-env file
  --only-env            only write .mina-env file, do not generate new keypair
  --len LEN             password length (hex digits, LEN >= 64)
  --pubkey              set MINA_PUBLIC_KEY env var
  --validate            validate the private key
  --pwd-fname PWD_FNAME
                        private key password file name (can only be used with --env and --only-env)
  --key-fname KEY_FNAME
                        wallet key file name (can only be used with --env and --only-env)
  --no-produce-blocks   do not produce blocks with MINA_PUBLIC_KEY, only connect to peers
  --import-account      import account
```

## [Mina start](./mina_start.sh)

Start a mina node instance

```sh
sh ./mina_start.sh
```

## [Mina snark](./mina_snark.sh)

Set the snark worker for a mina node

```sh
sh ./mina_snark.sh
```
