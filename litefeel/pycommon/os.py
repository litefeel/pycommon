import shlex
import subprocess
import sys
from typing import Iterable


# return (output, isOk)
def call(
    cmd: str, printOutput: bool = False, encoding: None | str | Iterable[str] = None
) -> tuple[str, bool]:
    # print(f"{printOutput = }, {cmd = }")
    if sys.platform == "win32":
        args = cmd
    else:
        # linux must split arguments
        args = shlex.split(cmd)
    try:
        if printOutput:
            isOk = subprocess.call(args) == 0
            return "", isOk

        data = subprocess.check_output(args)

        if encoding is None:
            encoding = "utf-8"

        itor = (encoding,) if isinstance(encoding, str) else encoding
        for enc in itor:
            try:
                output = data.decode(enc)
                isOk = True
                break
            except UnicodeDecodeError:
                pass
        return output, True
    except subprocess.CalledProcessError as callerr:
        print(f"cmd = {cmd}, callerr.output = {callerr.output}", file=sys.stderr)
        return (callerr.output, False)
    except IOError as ioerr:
        print(f"cmd = {cmd}, ioerr = {ioerr}", file=sys.stderr)
        return "", False
