#!/usr/bin/env python3

'version'

import importlib.metadata
import tomllib
from pathlib import Path


def _read_local_version() -> str | None:
    pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
    if not pyproject.is_file():
        return None

    with pyproject.open("rb") as f:
        data = tomllib.load(f)

    project = data.get("project")
    if isinstance(project, dict):
        version = project.get("version")
        if isinstance(version, str):
            return version
    return None


def _resolve_version() -> str:
    try:
        return importlib.metadata.version("litefeel-pycommon")
    except importlib.metadata.PackageNotFoundError:
        return _read_local_version() or "0.0.0"


__version__ = _resolve_version()
