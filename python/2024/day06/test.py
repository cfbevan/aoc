from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2
from .main import Map

input = ""
with open("day06/test_input.txt", "r") as fin:
    input = fin.read().strip()


class Testday06(TestCase):
    def test_map_parser(self):
        map = Map(input)
        self.assertEqual(len(map.data), 10)
        self.assertEqual(len(map.data[0]), 10)

    def test_pt1(self):
        output = pt1(input)
        expected = "41"
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = input
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
