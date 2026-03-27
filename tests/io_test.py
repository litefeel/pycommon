from unittest.mock import Mock, patch

from litefeel.pycommon.io import write_file


class TestIOMethods:
    def test_writefile(self):
        fake_file = Mock()
        fake_context = Mock()
        fake_context.__enter__ = Mock(return_value=fake_file)
        fake_context.__exit__ = Mock(return_value=None)

        with patch("litefeel.pycommon.io.makedirs") as makedirs, patch(
            "builtins.open", return_value=fake_context
        ) as open_mock:
            write_file("test.bin", b"aaaaa")

        makedirs.assert_called_once_with("test.bin", isfile=True)
        open_mock.assert_called_once_with("test.bin", mode="wb", encoding=None, newline=None)
        fake_file.write.assert_called_once_with(b"aaaaa")
