import unittest
import sys
#sys.path.insert(0, "../")

from litefeel.pycommon.color import Color, Color32, parse_color, parse_color32, _hex


class TestColorMethods(unittest.TestCase):
    def test_parse_color(self):
        # test
        # print(_split3('RGB'))
        # print(_split3('RRGGBB'))
        # print(_split4('RGBA'))
        # print(_split4('RRGGBBAA'))
        color = parse_color('0F0F0F')
        self.assertIsInstance(color, Color)
        self.assertEqual(color.html_rgba, '#0F0F0FFF')
        self.assertEqual(color.rgba, (0xF / 255, 0xF / 255, 0xF / 255, 1))
