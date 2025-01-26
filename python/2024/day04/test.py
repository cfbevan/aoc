from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2
from .main import WordSearch

input = ""
with open("day04/test_input.txt", "r") as fin:
    input = fin.read().strip()


class Testday04(TestCase):
    def test_word_search_get(self):
        ws = WordSearch("ABC\nDEF\nGHI")
        self.assertEqual(ws._get_dul(0, 0, 2), None)
        self.assertEqual(ws._get_u(0, 0, 2), None)
        self.assertEqual(ws._get_dur(0, 0, 2), None)
        self.assertEqual(ws._get_lr(0, 0, 2), "AB")
        self.assertEqual(ws._get_ddr(0, 0, 2), "AE")
        self.assertEqual(ws._get_d(0, 0, 2), "AD")
        self.assertEqual(ws._get_ddl(0, 0, 2), None)
        self.assertEqual(ws._get_rl(0, 0, 2), None)

        self.assertEqual(ws._get_dul(0, 1, 2), None)
        self.assertEqual(ws._get_u(0, 1, 2), None)
        self.assertEqual(ws._get_dur(0, 1, 2), None)
        self.assertEqual(ws._get_lr(0, 1, 2), "BC")
        self.assertEqual(ws._get_ddr(0, 1, 2), "BF")
        self.assertEqual(ws._get_d(0, 1, 2), "BE")
        self.assertEqual(ws._get_ddl(0, 1, 2), "BD")
        self.assertEqual(ws._get_rl(0, 1, 2), "BA")

        self.assertEqual(ws._get_dul(0, 2, 2), None)
        self.assertEqual(ws._get_u(0, 2, 2), None)
        self.assertEqual(ws._get_dur(0, 2, 2), None)
        self.assertEqual(ws._get_lr(0, 2, 2), None)
        self.assertEqual(ws._get_ddr(0, 2, 2), None)
        self.assertEqual(ws._get_d(0, 2, 2), "CF")
        self.assertEqual(ws._get_ddl(0, 2, 2), "CE")
        self.assertEqual(ws._get_rl(0, 2, 2), "CB")

        self.assertEqual(ws._get_dul(1, 0, 2), None)
        self.assertEqual(ws._get_u(1, 0, 2), "DA")
        self.assertEqual(ws._get_dur(1, 0, 2), "DB")
        self.assertEqual(ws._get_lr(1, 0, 2), "DE")
        self.assertEqual(ws._get_ddr(1, 0, 2), "DH")
        self.assertEqual(ws._get_d(1, 0, 2), "DG")
        self.assertEqual(ws._get_ddl(1, 0, 2), None)
        self.assertEqual(ws._get_rl(1, 0, 2), None)

        self.assertEqual(ws._get_dul(1, 1, 2), "EA")
        self.assertEqual(ws._get_u(1, 1, 2), "EB")
        self.assertEqual(ws._get_dur(1, 1, 2), "EC")
        self.assertEqual(ws._get_lr(1, 1, 2), "EF")
        self.assertEqual(ws._get_ddr(1, 1, 2), "EI")
        self.assertEqual(ws._get_d(1, 1, 2), "EH")
        self.assertEqual(ws._get_ddl(1, 1, 2), "EG")
        self.assertEqual(ws._get_rl(1, 1, 2), "ED")

        self.assertEqual(ws._get_dul(1, 2, 2), "FB")
        self.assertEqual(ws._get_u(1, 2, 2), "FC")
        self.assertEqual(ws._get_dur(1, 2, 2), None)
        self.assertEqual(ws._get_lr(1, 2, 2), None)
        self.assertEqual(ws._get_ddr(1, 2, 2), None)
        self.assertEqual(ws._get_d(1, 2, 2), "FI")
        self.assertEqual(ws._get_ddl(1, 2, 2), "FH")
        self.assertEqual(ws._get_rl(1, 2, 2), "FE")

        self.assertEqual(ws._get_dul(2, 0, 2), None)
        self.assertEqual(ws._get_u(2, 0, 2), "GD")
        self.assertEqual(ws._get_dur(2, 0, 2), "GE")
        self.assertEqual(ws._get_lr(2, 0, 2), "GH")
        self.assertEqual(ws._get_ddr(2, 0, 2), None)
        self.assertEqual(ws._get_d(2, 0, 2), None)
        self.assertEqual(ws._get_ddl(2, 0, 2), None)
        self.assertEqual(ws._get_rl(2, 0, 2), None)

        self.assertEqual(ws._get_dul(2, 1, 2), "HD")
        self.assertEqual(ws._get_u(2, 1, 2), "HE")
        self.assertEqual(ws._get_dur(2, 1, 2), "HF")
        self.assertEqual(ws._get_lr(2, 1, 2), "HI")
        self.assertEqual(ws._get_ddr(2, 1, 2), None)
        self.assertEqual(ws._get_d(2, 1, 2), None)
        self.assertEqual(ws._get_ddl(2, 1, 2), None)
        self.assertEqual(ws._get_rl(2, 1, 2), "HG")

        self.assertEqual(ws._get_dul(2, 2, 2), "IE")
        self.assertEqual(ws._get_u(2, 2, 2), "IF")
        self.assertEqual(ws._get_dur(2, 2, 2), None)
        self.assertEqual(ws._get_lr(2, 2, 2), None)
        self.assertEqual(ws._get_ddr(2, 2, 2), None)
        self.assertEqual(ws._get_d(2, 2, 2), None)
        self.assertEqual(ws._get_ddl(2, 2, 2), None)
        self.assertEqual(ws._get_rl(2, 2, 2), "IH")

    def test_word_search(self):
        ws = WordSearch("MMM\nMXM\nMMM")
        self.assertEqual(ws._check(1, 1, "XM"), 8)

    def test_pt1(self):
        output = pt1(input)
        expected = "18"
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = "9"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
