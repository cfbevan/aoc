from unittest import TestCase
from unittest import main

from .main import pt1
from .main import safe
from .main import pt2

input = ""
with open("day02/test_input.txt", "r") as fin:
    input = fin.read().strip()


class Testday02(TestCase):
    def test_safe(self):
        self.assertTrue(safe([7, 6, 4, 2, 1]))
        self.assertFalse(safe([1, 2, 7, 8, 9]))
        self.assertFalse(safe([9, 7, 6, 2, 1]))
        self.assertFalse(safe([1, 3, 2, 4, 5]))
        self.assertFalse(safe([8, 6, 4, 4, 1]))
        self.assertTrue(safe([1, 3, 6, 7, 9]))

    def test_pt1(self):
        output = pt1(input)
        expected = "2"
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = "4"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
