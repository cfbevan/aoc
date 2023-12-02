from unittest import TestCase
from unittest import main

from .main import Game
from .main import pt1
from .main import pt2

input = ""
with open("day02/test_input.txt", "r") as fin:
    input = fin.read().strip()


class Testday02(TestCase):
    def test_parse(self):
        g = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(g.id, 1)
        self.assertEqual(len(g.rounds), 3)
        self.assertEqual(g.rounds[0].red, 4)
        self.assertEqual(g.rounds[0].green, 0)
        self.assertEqual(g.rounds[0].blue, 3)
        self.assertEqual(g.rounds[1].red, 1)
        self.assertEqual(g.rounds[1].green, 2)
        self.assertEqual(g.rounds[1].blue, 6)
        self.assertEqual(g.rounds[2].red, 0)
        self.assertEqual(g.rounds[2].green, 2)
        self.assertEqual(g.rounds[2].blue, 0)
        self.assertEqual(g.red, 4)
        self.assertEqual(g.green, 2)
        self.assertEqual(g.blue, 6)
        self.assertEqual(g.power, 4 * 2 * 6)

    def test_pt1(self):
        output = pt1(input)
        expected = 8
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 2286
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
