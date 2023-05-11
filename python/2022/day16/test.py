from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2

input = ''
with open('day16/test_input.txt', 'r') as fin:
    input = fin.read().strip()

class Testday16(TestCase):

    def test_pt1(self):
        output = pt1(input)
        expected = input
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = input
        self.assertEqual(output, expected)
        
if __name__ == '__main__':
    main()