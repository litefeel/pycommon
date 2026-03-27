import pytest

from litefeel.pycommon.color import Color, parse_color, parse_color32


class TestColorMethods:
    def test_parse_color(self):
        color = parse_color("0F0F0F")
        assert isinstance(color, Color)
        assert color.html_rgba == "#0F0F0FFF"
        assert color.rgba == (0xF / 255, 0xF / 255, 0xF / 255, 1)

    def test_parse_color32_shorthand_rgba(self):
        color = parse_color32("#abcd")

        assert color.html_rgba == "#AABBCCDD"

    def test_parse_color_invalid_length_raises_value_error(self):
        with pytest.raises(ValueError, match="incorrect format for color"):
            parse_color32("12")
