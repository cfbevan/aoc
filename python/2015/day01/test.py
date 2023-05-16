from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2


class Testday01(TestCase):
    def test_pt1_ex1(self):
        output = pt1("(())")
        expected = 0
        self.assertEqual(output, expected)

    def test_pt1_ex2(self):
        output = pt1("()()")
        expected = 0
        self.assertEqual(output, expected)

    def test_pt1_ex3(self):
        output = pt1("(((")
        expected = 3
        self.assertEqual(output, expected)

    def test_pt1_ex4(self):
        output = pt1("(()(()(")
        expected = 3
        self.assertEqual(output, expected)

    def test_pt1_ex5(self):
        output = pt1("))(((((")
        expected = 3
        self.assertEqual(output, expected)

    def test_pt1_ex6(self):
        output = pt1("())")
        expected = -1
        self.assertEqual(output, expected)

    def test_pt1_ex7(self):
        output = pt1("))(")
        expected = -1
        self.assertEqual(output, expected)

    def test_pt1_ex8(self):
        output = pt1(")))")
        expected = -3
        self.assertEqual(output, expected)

    def test_pt1_ex9(self):
        output = pt1(")())())")
        expected = -3
        self.assertEqual(output, expected)

    def test_pt2_ex1(self):
        output = pt2(")")
        expected = 1
        self.assertEqual(output, expected)

    def test_pt2_ex2(self):
        output = pt2("()())")
        expected = 5
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
