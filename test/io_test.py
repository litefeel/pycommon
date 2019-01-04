from litefeel.pycommon.io import write_file


class TestIOMethods:
    def test_writefile(self):
        write_file("test.bin", b"aaaaa")
