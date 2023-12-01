from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2
from .main import line_to_digit
from .main import line_to_digit2

input = ""
with open("day01/test_input.txt", "r") as fin:
    input = fin.read().strip()

input2 = ""
with open("day01/test_input2.txt", "r") as fin:
    input2 = fin.read().strip()


class Testday01(TestCase):
    def test_line_to_digit(self):
        self.assertEqual(line_to_digit("1abc2"), 12)
        self.assertEqual(line_to_digit("pqr3stu8vwx"), 38)
        self.assertEqual(line_to_digit("a1b2c3d4e5f"), 15)
        self.assertEqual(line_to_digit("treb7uchet"), 77)

    def test_pt1(self):
        output = pt1(input)
        expected = 142
        self.assertEqual(output, expected)

    def test_line_to_digit2(self):
        self.assertEqual(line_to_digit2("two1nine"), 29)
        self.assertEqual(line_to_digit2("eightwothree"), 83)
        self.assertEqual(line_to_digit2("abcone2threexyz"), 13)
        self.assertEqual(line_to_digit2("xtwone3four"), 24)
        self.assertEqual(line_to_digit2("4nineeightseven2"), 42)
        self.assertEqual(line_to_digit2("zoneight234"), 14)
        self.assertEqual(line_to_digit2("7pqrstsixteen"), 76)
        self.assertEqual(line_to_digit2("eightwo"), 82)

    def test_pt2(self):
        output = pt2(input2)
        expected = 281
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
