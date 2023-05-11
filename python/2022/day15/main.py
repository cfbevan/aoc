from __future__ import annotations
from logging import getLogger, basicConfig
from re import compile
from utils.point import Pt
from utils.size import Size
from functools import cached_property
from dataclasses import dataclass

import numpy

logger = getLogger(__name__)
basicConfig(level='ERROR')

row_re = compile(r'[xy]=(-?\d+)')

@dataclass(eq=True,frozen=True)
class Sensor:
    position: Pt
    beacon: Pt

    @cached_property
    def min_distance(self) -> float:
        return self.position.manhattan_distance(self.beacon)

    def __iter__(self):
        yield self.position
        yield self.beacon

    def frequency(self) -> int:
        return self.beacon.x * 4000000 + self.beacon.y

class Zone:

    def __init__(self, data: str) -> None:
        self.sensors: set[Sensor] = set()
        self.size_x = Size()
        self.size_y = Size()
        self.size_d = Size()
        self._parse(data)

    def _parse(self, data: str) -> None:
        logger.debug('==Parsing')
        for row in data.split('\n'):
            try:
                (x1,y1,x2,y2) = row_re.findall(row.strip())
            except Exception as e:
                logger.error(row)
                logger.error(row_re.findall(row.strip()))
                logger.exception(e)
            s = Pt(int(x1), int(y1))
            b = Pt(int(x2), int(y2))
            self.sensors.add(Sensor(s,b))
            logger.debug('-sensor %s', s)
            logger.debug('-beacon %s', b)
            # update size
            self.size_x.update(s.x, b.x)
            self.size_y.update(s.y, b.y)
            # exclude points
            dist = s.manhattan_distance(b)
            self.size_d.update(dist)
            logger.debug('    distance: %s', dist)

    def positions_excluded(self, row: int):
        M = numpy.arange(
            self.size_x.min - self.size_d.max,
            self.size_x.max + self.size_d.max
        ) + complex(0,row)
        R = M==None
        for s in self.sensors:
            N = M - complex(s.position)
            N = abs(N.real) + abs(N.imag)
            R |=  (N<=s.min_distance)&(M!=complex(s.beacon))
        return R.sum()

def pt1(input: str) -> int:
    z = Zone(input)
    return z.positions_excluded(2000000)

def pt2(input: str) -> str:
    return input

if __name__ == '__main__':
    with open('day15/input.txt', 'r') as fin:
        input = fin.read().strip()
        print(pt1(input))
        #print(pt2(input))
