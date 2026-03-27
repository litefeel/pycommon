import io
import os
from unittest import mock

from litefeel.pycommon import ftp as ftp_module


class _FakeFTPClient:
    def __init__(self):
        self.cwd_calls = []
        self.mkd_calls = []
        self.stored = []

    def cwd(self, path: str):
        self.cwd_calls.append(path)

    def mkd(self, path: str):
        self.mkd_calls.append(path)

    def storbinary(self, command: str, stream):
        self.stored.append((command, stream.read()))


def test_try_push_dir_creates_remote_dir_before_listing(monkeypatch):
    calls = []
    fake_client = _FakeFTPClient()
    ftp = object.__new__(ftp_module.FTP)
    ftp._ftp = fake_client

    def fake_makedirs(client, path, remote_dirs):
        calls.append(("makedirs", path))

    def fake_list_all(self, path):
        calls.append(("list_all", path))
        return [], [], []

    def fake_walk(path):
        assert path == "local_dir"
        return [("local_dir", [], ["file.txt"])]

    monkeypatch.setattr(ftp_module, "_makedirs", fake_makedirs)
    monkeypatch.setattr(ftp_module.FTP, "list_all", fake_list_all)
    monkeypatch.setattr(os, "walk", fake_walk)

    with mock.patch("builtins.open", return_value=io.BytesIO(b"data")):
        ftp.try_push_dir("local_dir", "/remote")

    assert calls[:2] == [("makedirs", "/remote"), ("list_all", "/remote")]
    assert fake_client.stored == [("STOR file.txt", b"data")]
