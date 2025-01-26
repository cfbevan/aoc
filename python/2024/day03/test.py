from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2


class Testday03(TestCase):
    def test_pt1(self):
        with open("day03/test_input.txt", "r") as fin:
            input = fin.read().strip()
        output = pt1(input)
        expected = "161"
        self.assertEqual(output, expected)

    def test_pt2(self):
        with open("day03/test_input2.txt", "r") as fin:
            input = fin.read().strip()
        output = pt2(input)
        expected = "48"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
