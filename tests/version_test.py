import importlib.metadata

from litefeel import pycommon


def test_resolve_version_falls_back_to_local_pyproject(monkeypatch):
    def raise_package_not_found(_: str):
        raise importlib.metadata.PackageNotFoundError

    monkeypatch.setattr(importlib.metadata, "version", raise_package_not_found)

    assert pycommon._resolve_version() == "0.4.18"
