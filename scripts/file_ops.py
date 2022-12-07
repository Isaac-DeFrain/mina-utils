import os
import pathlib

def mkdir(dir_path: pathlib.Path):
    '''
    Creates the dir if it doesn't already exist
    '''
    if not dir_path.exists():
        os.system(f"mkdir {dir_path}")
