from file_ops import *
from pathlib import Path
from wallet_template import *
from secrets import token_hex
from os import environ, listdir, system
from argparse import ArgumentParser

SECRETS = Path(__file__).parent.parent / "secrets"
ENV_DIR = Path("~/.mina_env")
KEYS_DIR = Path("~/.mina_keys")

def new_wallet_file(wallet_fname: str) -> int:
    return int(wallet_fname.split(".")[0][0])

def is_wallet(fname: str) -> bool:
    fields = fname.split(".")
    return len(fields) > 1 and fields[1] == "wallet"

def new_pwd_and_wallet_paths(n: int) -> tuple[Path, Path]:
    '''
    Returns (`pwd_path`, `wallet_path`)
    '''
    return SECRETS / f"{n}.pwd", SECRETS / f"{n}.wallet"

def gen_pwd(n: int, length: int = 64) -> str:
    pwd = ""
    if not (SECRETS / f"{n}.pwd").exists():
        if not length or length < 64:
            length = 64
        pwd_path, _ = new_pwd_and_wallet_paths(n)
        system(f"touch {pwd_path}")
        with pwd_path.open("w", encoding="utf-8") as f:
            pwd = token_hex(length)
            f.write(pwd)
            f.close()
    return pwd

def gen_mina_wallet_paths(n: int) -> tuple[Path, Path]:
    '''
    Returns (`root_wallet_path`, `local_wallet_path`)
    '''
    _, wallet_path = new_pwd_and_wallet_paths(n)
    root_wallet_path = KEYS_DIR / f"{n}.wallet"
    system(f"touch {wallet_path}")
    return root_wallet_path, wallet_path

def clean_up_wallet_file(wpath: Path):
    with wpath.open("r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    with wpath.open("w", encoding="utf-8") as f:
        f.write(lines[-2] + lines[-1])
        f.close()

# def mina_env(): pass

# parser

if __name__ == "__main__":
    parser = ArgumentParser(description="mina wallet password generator")
    parser.add_argument("--len", action="store", nargs=1, help="password length (number of hex digits, must be >= 64)")
    parser.add_argument("--validate", action="store_true", help="validate the private key")
    parser.add_argument("input", action="store", nargs="*")
    args = parser.parse_args()
    mkdir(SECRETS)
    mkdir(KEYS_DIR)
    wallet_files = list(filter(is_wallet, listdir(SECRETS)))
    n = 1 + max([new_wallet_file(wname) for wname in wallet_files]) if wallet_files else 0
    system(f"chmod 700 {KEYS_DIR}")
    root_wallet_path, wallet_path = gen_mina_wallet_paths(n)
    pwd = gen_pwd(n, int(args.len[0])) if args.len else gen_pwd(n)
    environ["MINA_PRIVKEY_PASS"] = pwd
    system(f"mina-generate-keypair --privkey-path {root_wallet_path} > {wallet_path}")
    if args.validate:
        system(f"mina-validate-keypair --privkey-path {root_wallet_path}")
    environ.pop("MINA_PRIVKEY_PASS")
    clean_up_wallet_file(wallet_path)
    system(f"chmod 600 {SECRETS}")
    system(f"chmod 600 {KEYS_DIR}")
