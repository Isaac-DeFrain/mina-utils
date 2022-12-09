# Mina scripts

## Keypair generation

Run all commands from `mina-utils/scripts`!

### Usage

```bash
$ cd scripts
$ python -m mina_gen_keypair --help
usage: mina_gen_keypair.py [-h] [--len LEN] [--validate] [input ...]

mina wallet password generator

positional arguments:
  input

optional arguments:
  -h, --help  show this help message and exit
  --len LEN   password length (number of hex digits, must be >= 64)
  --validate  validate the private key
```

### Basic usage

- generates 64 hex digit password
- does not validate private key

```bash
$ python -m mina_gen_keypair
```

### Supply password length

- `LEN >= 64` or 64 will be used by default
- does not validate private key

```bash
$ python -m mina_gen_keypair --len LEN
```

### Validate private key

```bash
$ python -m mina_gen_keypair --validate
```
