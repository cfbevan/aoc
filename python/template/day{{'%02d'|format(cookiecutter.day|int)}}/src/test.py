from unittest import TestCase
from unittest import main

from src.main import pt1
from src.main import pt2

with open("../test_input.txt", "r") as fin:
    input = fin.read().strip()

class Testday01(TestCase):

    def test_pt1(self):
        output = pt1(input)
        expected = ''
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = ''
        self.assertEqual(output, expected)
        
if __name__ == '__main__':
    main()