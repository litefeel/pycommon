from litefeel.pycommon.color import (Color, Color32, _hex, parse_color,
                                     parse_color32)


class TestColorMethods:
    def test_parse_color(self):
        # print(_split3('RGB'))
        # print(_split3('RRGGBB'))
        # print(_split4('RGBA'))
        # print(_split4('RRGGBBAA'))
        color = parse_color('0F0F0F')
        assert isinstance(color, Color)
        assert color.html_rgba == '#0F0F0FFF'
        assert color.rgba == (0xF / 255, 0xF / 255, 0xF / 255, 1)
