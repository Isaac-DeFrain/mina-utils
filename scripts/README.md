# Mina scripts

Run all commands from here (`mina-utils/scripts`)

## [Mina keypair generation](./mina_gen_keypair.py)

Python script for generating cryptographically secure passwords, keypairs, and env file for mina

```sh
$ python -m mina_gen_keypair --help
usage: mina_gen_keypair.py [-h] [--env] [--len LEN] [--validate] [input ...]

Mina keypair generator

positional arguments:
  input

optional arguments:
  -h, --help  show this help message and exit
  --env       write .mina-env file
  --len LEN   password length (hex digits, LEN >= 64)
  --validate  validate the private key
```

## [Mina start](./mina_start.sh)

Start a mina node instance

```sh
sh ./mina_start.sh
```
