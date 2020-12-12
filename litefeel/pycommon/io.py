"some function for io"

import os
import shutil


def makedirs(filename, isfile=False):
    "like os.makedirs, can pass a filename"
    dirname = os.path.dirname(filename) if isfile else filename
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)


def write_file(filename, data, mode=None, encoding="utf-8", newline=None):
    "save data to file"
    makedirs(filename, isfile=True)
    if not mode:
        mode = "w" if isinstance(data, str) else "wb"
    if isinstance(data, (bytearray, bytes)):
        encoding = None
        newline = None
    with open(filename, mode=mode, encoding=encoding, newline=newline) as f:
        f.write(data)


def read_file(filename, isbin=False, encoding="utf-8"):
    "read data from file"
    mode = "rb" if isbin else "r"
    with open(filename, mode=mode, encoding=encoding) as f:
        return f.read()


def copy_file(src, dst):
    makedirs(dst, True)
    shutil.copyfile(src, dst)
