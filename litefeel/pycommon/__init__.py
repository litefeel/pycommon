#!/usr/bin/env python3

'version'

import importlib.metadata
import re
from pathlib import Path


def _read_local_version() -> str | None:
    pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
    if not pyproject.is_file():
        return None

    match = re.search(r'^version\s*=\s*"([^"]+)"\s*$', pyproject.read_text(encoding="utf-8"), re.MULTILINE)
    if match:
        return match.group(1)
    return None


def _resolve_version() -> str:
    try:
        return importlib.metadata.version("litefeel-pycommon")
    except importlib.metadata.PackageNotFoundError:
        return _read_local_version() or "0.0.0"


__version__ = _resolve_version()
