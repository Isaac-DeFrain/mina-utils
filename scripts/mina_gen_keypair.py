import os
import sys
import pathlib
import secrets
import argparse
import file_ops

PathPair = tuple[pathlib.Path, pathlib.Path]

HOME_DIR = pathlib.Path(input("Set your home directory: "))

SECRETS_DIR = pathlib.Path(__file__).parent.parent / "secrets"
KEYS_DIR = HOME_DIR / ".mina-keys"
ENV_PATH = HOME_DIR / ".mina-env" # this is a file

##### password and wallets #####

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

def get_pubkey(key_name: str) -> str:
    wallet_path = SECRETS_DIR / f"{key_name}.wallet"
    with wallet_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    return lines[0].split(":")[1].strip()

##### mina env #####

def env_template(
        produce_blocks: bool,
        pwd: str,
        wallet_key_path: pathlib.Path,
        log_level: str = "Info",
        file_log_level: str = "Debug",
        peer_list_url: str = "https://storage.googleapis.com/mina-seed-lists/mainnet_seeds.txt") -> str:
    '''
    Mina env template

    Sets `MINA_PRIVKEY_PASS`, `LOG_LEVEL`, `FILE_LOG_LEVEL`, `EXTRA_FLAGS`, `PEER_LIST_URL`
    '''
    if produce_blocks:
        env_contents = f'''\
MINA_PRIVKEY_PASS="{pwd}"
LOG_LEVEL={log_level}
FILE_LOG_LEVEL={file_log_level}
EXTRA_FLAGS=" --block-producer-key {wallet_key_path}"
PEER_LIST_URL={peer_list_url}
'''
    else:
        env_contents = f'PEER_LIST_URL={peer_list_url}\n'
    return env_contents

def mina_env(produce_blocks: bool, pwd_fname: str = "0", key_fname: str = "0"):
    '''
    Mina env template

    Sets `MINA_PRIVKEY_PASS`, `EXTRA_FLAGS`, `LOG_LEVEL`, `FILE_LOG_LEVEL`, `PEER_LIST_URL` (requires 700 permissions)
    '''
    pwd_path = SECRETS_DIR / f"{pwd_fname}.pwd"
    key_path = KEYS_DIR / f"{key_fname}.wallet"
    if not pwd_path.exists():
        print(f"Error: the provided password ({pwd_path}) does not exist. Exiting...")
        sys.exit(1)
    pwd = file_ops.read(pwd_path)
    file_ops.write(ENV_PATH, env_template(produce_blocks, pwd, key_path))

##### parser #####

def check(args: argparse.Namespace):
    # --env and --only-env
    if args.pwd_fname and not (args.env or args.only_env):
        print("--pwd-fname can only be used with --env or --env-only")
        sys.exit(1)
    if args.key_fname and not (args.env or args.only_env):
        print("--key-fname can only be used with --env or --env-only")
        sys.exit(1)
    if args.produce_blocks and not (args.env or args.only_env):
        print("--produce-blocks can only be used with --env or --env-only")
        sys.exit(1)

def init_mina_env(args: argparse.Namespace):
    if args.pwd_fname and args.key_fname:
        mina_env(args.produce_blocks, args.pwd_fname[0], args.key_fname[0])
    elif args.pwd_fname:
        mina_env(args.produce_blocks, pwd_fname=args.pwd_fname[0])
    elif args.key_fname:
        mina_env(args.produce_blocks, key_fname=args.key_fname[0])
    else:
        mina_env(args.produce_blocks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mina keypair generator")
    parser.add_argument("--env", action="store_true", help="write .mina-env file")
    parser.add_argument("--only-env", action="store_true", help="only write .mina-env file, do not generate new keypair")
    parser.add_argument("--len", action="store", nargs=1, help="password length (hex digits, LEN >= 64)")
    parser.add_argument("--validate", action="store_true", help="validate the private key")
    parser.add_argument("--pwd-fname", action="store", nargs=1, help="private key password file name (can only be used with --env and --only-env)")
    parser.add_argument("--key-fname", action="store", nargs=1, help="wallet key file name (can only be used with --env and --only-env)")
    parser.add_argument("--produce-blocks", action="store_true", help="produce blocks")
    parser.add_argument("input", action="store", nargs="*")
    args = parser.parse_args()
    check(args)
    if args.only_env:
        init_mina_env(args)
    else:
        file_ops.mkdir(SECRETS_DIR)
        file_ops.mkdir(KEYS_DIR)
        os.system(f"chmod 700 {SECRETS_DIR}")
        os.system(f"chmod 700 {KEYS_DIR}")
        wallet_files = list(filter(is_wallet, os.listdir(SECRETS_DIR)))
        n = 1 + max([new_wallet_file(wname) for wname in wallet_files]) if wallet_files else 0
        root_wallet_path, wallet_path = gen_mina_wallet_paths(n)
        pwd = gen_pwd(str(n), int(args.len[0])) if args.len else gen_pwd(str(n))
        os.environ["MINA_PRIVKEY_PASS"] = pwd
        os.system(f"mina-generate-keypair --privkey-path {root_wallet_path} > {wallet_path}")
        if args.validate:
            os.system(f"mina-validate-keypair --privkey-path {root_wallet_path}")
        if args.env:
            init_mina_env(args)
        os.environ.pop("MINA_PRIVKEY_PASS")
        os.environ["MINA_PUBLIC_KEY"] = get_pubkey(str(n))
        clean_up_wallet_file(wallet_path)
        os.system(f"chmod 600 {SECRETS_DIR}")
        os.system(f"chmod 600 {KEYS_DIR}")
