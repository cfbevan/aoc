from unittest import TestCase
from unittest import main

from .main import Point
from .main import GearMap
from .main import pt1
from .main import pt2

input = ""
with open("day03/test_input.txt", "r") as fin:
    input = fin.read().strip()


input2 = ""
with open("day03/test_input2.txt", "r") as fin:
    input = fin.read().strip()

input3 = ""
with open("day03/test_input3.txt", "r") as fin:
    input = fin.read().strip()


class Testday03(TestCase):
    def test_adjacent(self):
        self.assertTrue(Point(0, 0).adjacent(Point(0, 0)))
        self.assertTrue(Point(0, 0).adjacent(Point(0, 1)))
        self.assertTrue(Point(0, 0).adjacent(Point(1, 0)))
        self.assertTrue(Point(0, 0).adjacent(Point(1, 1)))
        self.assertTrue(Point(1, 1).adjacent(Point(0, 0)))
        self.assertTrue(Point(1, 1).adjacent(Point(0, 1)))
        self.assertTrue(Point(1, 1).adjacent(Point(0, 2)))
        self.assertTrue(Point(1, 1).adjacent(Point(1, 0)))
        self.assertTrue(Point(1, 1).adjacent(Point(1, 1)))
        self.assertTrue(Point(1, 1).adjacent(Point(1, 2)))
        self.assertTrue(Point(1, 1).adjacent(Point(2, 0)))
        self.assertTrue(Point(1, 1).adjacent(Point(2, 1)))
        self.assertTrue(Point(1, 1).adjacent(Point(2, 2)))
        self.assertFalse(Point(0, 0).adjacent(Point(0, 2)))

    def test_pt1_input1(self):
        output = pt1(input)
        expected = 4361
        self.assertEqual(output, expected)

    def test_pt1_input2(self):
        output = pt1(input2)
        expected = 413
        self.assertEqual(output, expected)

    def test_pt1_input3(self):
        output = pt1(input3)
        expected = 925
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = input
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
