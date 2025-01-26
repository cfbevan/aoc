from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2
from .main import PrintQueue

input = ""
with open("day05/test_input.txt", "r") as fin:
    input = fin.read().strip()


class Testday05(TestCase):
    def test_print_queue_parser(self):
        pq = PrintQueue(input)
        self.assertEqual(pq.rules[47], [53, 13, 61, 29])
        self.assertEqual(pq.rules[97], [13, 61, 47, 29, 53, 75])
        self.assertEqual(pq.rules[75], [29, 53, 47, 61, 13])
        self.assertEqual(pq.rules[61], [13, 53, 29])
        self.assertEqual(pq.rules[29], [13])
        self.assertEqual(pq.rules[53], [29, 13])
        self.assertEqual(
            pq.jobs,
            [
                [75, 47, 61, 53, 29],
                [97, 61, 53, 29, 13],
                [75, 29, 13],
                [75, 97, 47, 61, 53],
                [61, 13, 29],
                [97, 13, 75, 29, 47],
            ],
        )

    def test_check_job(self):
        pq = PrintQueue(input)
        self.assertTrue(pq._check_job([75, 47, 61, 53, 29]))
        self.assertTrue(pq._check_job([97, 61, 53, 29, 13]))
        self.assertTrue(pq._check_job([75, 29, 13]))
        self.assertFalse(pq._check_job([75, 97, 47, 61, 53]))
        self.assertFalse(pq._check_job([61, 13, 29]))
        self.assertFalse(pq._check_job([97, 13, 75, 29, 47]))

    def test_correct_jobs(self):
        pq = PrintQueue(input)
        self.assertEqual(
            pq.correct_jobs, [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]
        )

    def test_incorrect_jobs(self):
        pq = PrintQueue(input)
        self.assertEqual(
            pq.incorrect_jobs,
            [[75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]],
        )

    def test_fix_job(self):
        pq = PrintQueue(input)
        self.assertEqual(pq.fix_job([75, 97, 47, 61, 53]), [97, 75, 47, 61, 53])
        self.assertEqual(pq.fix_job([61, 13, 29]), [61, 29, 13])
        self.assertEqual(pq.fix_job([97, 13, 75, 29, 47]), [97, 75, 47, 29, 13])

    def test_pt1(self):
        output = pt1(input)
        expected = "143"
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = "123"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
