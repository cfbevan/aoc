from unittest import TestCase
from unittest import main

from .main import Box


class Testday02(TestCase):
    def test_box_pt1_ex1(self):
        output = Box("2x3x4").wrapping_paper()
        expected = 58
        self.assertEqual(output, expected)

    def test_box_pt1_ex2(self):
        output = Box("1x1x10").wrapping_paper()
        expected = 43
        self.assertEqual(output, expected)

    def test_box_pt2_ex1(self):
        output = Box("2x3x4").ribbon()
        expected = 34
        self.assertEqual(output, expected)

    def test_box_pt2_ex2(self):
        output = Box("1x1x10").ribbon()
        expected = 14
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
