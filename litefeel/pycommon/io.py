"some function for io"

import codecs
import locale
import os
import shutil
import sys


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


def _correct_print(isstdout):
    """correct"""
    stream = sys.stdout if isstdout else sys.stderr
    if stream.encoding.upper() != "UTF-8":
        encoding = stream.encoding or locale.getpreferredencoding()
        try:
            encoder = codecs.getwriter(encoding)
        except LookupError:
            encoder = codecs.getwriter("UTF-8")
        try:
            newstream = encoder(stream.buffer, "xmlcharrefreplace")
        except AttributeError:
            newstream = encoder(stream, "xmlcharrefreplace")
        if isstdout:
            sys.stdout = newstream
        else:
            sys.stderr = newstream


# correct print
# must call in app start
def correct_print(stdout=True, stderr=True):
    if stdout:
        _correct_print(True)
    if stderr:
        _correct_print(False)
