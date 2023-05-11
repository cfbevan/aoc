from unittest import TestCase
from unittest import main

from utils.point import Pt
from .main import Zone

input = ''
with open('day15/test_input.txt', 'r') as fin:
    input = fin.read().strip()

class Testday15(TestCase):

    def test_distance(self):
        self.assertEqual(
            Pt(0,0).manhattan_distance(Pt(1,0)),
            1
        )
        self.assertEqual(
            Pt(0,0).manhattan_distance(Pt(-1,0)),
            1
        )
        self.assertEqual(
            Pt(0,0).manhattan_distance(Pt(0,1)),
            1
        )
        self.assertEqual(
            Pt(0,0).manhattan_distance(Pt(0,-1)),
            1
        )
        self.assertEqual(
            Pt(0,0).manhattan_distance(Pt(1,1)),
            2
        )
        self.assertEqual(
            Pt(0,0).manhattan_distance(Pt(-1,-1)),
            2
        )

    def test_complex(self):
        self.assertEqual(
            complex(Pt(1,1)),
            1+1j,
        )
        self.assertEqual(
            complex(Pt(-1,10)),
            -1+10j
        )

    def test_positions_excluded(self):
        z = Zone(input)
        self.assertEqual(z.positions_excluded(10), 26)
        
if __name__ == '__main__':
    main()