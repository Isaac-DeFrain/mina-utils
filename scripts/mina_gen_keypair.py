import os
import pathlib
import secrets
import argparse
import file_ops

PathPair = tuple[pathlib.Path, pathlib.Path]

SECRETS_DIR = pathlib.Path(__file__).parent.parent / "secrets"
KEYS_DIR = pathlib.Path("~/.mina-keys")
ENV_PATH = pathlib.Path("~/.mina-env") # this is a file

def new_wallet_file(wallet_fname: str) -> int:
    try:
        res = int(wallet_fname.split(".")[0])
    except ValueError:
        res = -1
    return res

def is_wallet(fname: str) -> bool:
    try:
        res = fname.split(".")[1] == "wallet"
    except:
        res = False
    return res

def new_pwd_and_wallet_paths(n: int) -> PathPair:
    '''
    Returns (`pwd_path`, `wallet_path`)
    '''
    return SECRETS_DIR / f"{n}.pwd", SECRETS_DIR / f"{n}.wallet"

def gen_pwd(pwd_file: str, length: int = 64) -> str:
    pwd_path0 = SECRETS_DIR / f"{pwd_file}.pwd"
    if pwd_path0.exists():
        pwd = file_ops.read(pwd_path0)
    else:
        if not length or length < 64:
            length = 64
        pwd = secrets.token_hex(length)
        pwd_path, _ = new_pwd_and_wallet_paths(n)
        file_ops.write(pwd_path, pwd)
    return pwd

def gen_mina_wallet_paths(n: int) -> PathPair:
    '''
    Returns (`root_wallet_path`, `local_wallet_path`)
    '''
    _, wallet_path = new_pwd_and_wallet_paths(n)
    root_wallet_path = KEYS_DIR / f"{n}.wallet"
    os.system(f"touch {wallet_path}")
    return root_wallet_path, wallet_path

def clean_up_wallet_file(wpath: pathlib.Path):
    with wpath.open("r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    file_ops.write(wpath, lines[-2] + lines[-1])

# mina env

def env_template(
        pwd: str,
        wallet_key_path: pathlib.Path,
        log_level: str = "Info",
        file_log_level: str = "Debug",
        peer_list_url: str = "https://storage.googleapis.com/mina-seed-lists/mainnet_seeds.txt") -> str:
    '''
    Mina env template

    Sets `MINA_PRIVKEY_PASS`, `LOG_LEVEL`, `FILE_LOG_LEVEL`, `EXTRA_FLAGS`, `PEER_LIST_URL`
    '''
    return f'''\
MINA_PRIVKEY_PASS="{pwd}"
LOG_LEVEL={log_level}
FILE_LOG_LEVEL={file_log_level}
EXTRA_FLAGS=" --block-producer-key {wallet_key_path}"
PEER_LIST_URL={peer_list_url}
'''

def mina_env(
        pwd_path: pathlib.Path = SECRETS_DIR / "0.pwd",
        wallet_key_path: pathlib.Path = KEYS_DIR / "0.wallet"):
    '''
    Mina env template

    Sets `MINA_PRIVKEY_PASS`, `EXTRA_FLAGS`, `LOG_LEVEL`, `FILE_LOG_LEVEL`, `PEER_LIST_URL`

    Requires 700 permissions
    '''
    pwd = file_ops.read(pwd_path)
    file_ops.write(ENV_PATH, env_template(pwd, wallet_key_path))

# parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mina keypair generator")
    parser.add_argument("--env", action="store_true", help="write .mina-env file")
    parser.add_argument("--len", action="store", nargs=1, help="password length (hex digits, LEN >= 64)")
    parser.add_argument("--validate", action="store_true", help="validate the private key")
    parser.add_argument("input", action="store", nargs="*")
    args = parser.parse_args()
    file_ops.mkdir(SECRETS_DIR)
    file_ops.mkdir(KEYS_DIR)
    os.system(f"chmod 700 {SECRETS_DIR}")
    os.system(f"chmod 700 {KEYS_DIR}")
    wallet_files = list(filter(is_wallet, os.listdir(SECRETS_DIR)))
    n = 1 + max([new_wallet_file(wname) for wname in wallet_files]) if wallet_files else 0
    root_wallet_path, wallet_path = gen_mina_wallet_paths(n)
    pwd = gen_pwd(str(n), int(args.len[0])) if args.len else gen_pwd(str(n))
    # use env var for password
    os.environ["MINA_PRIVKEY_PASS"] = pwd
    os.system(f"mina-generate-keypair --privkey-path {root_wallet_path} > {wallet_path}")
    if args.validate:
        os.system(f"mina-validate-keypair --privkey-path {root_wallet_path}")
    if args.env:
        mina_env()
    os.environ.pop("MINA_PRIVKEY_PASS")
    clean_up_wallet_file(wallet_path)
    os.system(f"chmod 600 {SECRETS_DIR}")
    os.system(f"chmod 600 {KEYS_DIR}")
