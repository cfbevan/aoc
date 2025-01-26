from dataclasses import dataclass

ascii_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"Pt({self.x},{self.y})"

    def manhattan_distance(self, __o: "Point") -> int:
        return abs(self.x - __o.x) + abs(self.y - __o.y)

    def adjacent(self, pt: "Point") -> bool:
        return (pt.x - 1 <= self.x <= pt.x + 1) and (pt.y - 1 <= self.y <= pt.y + 1)


@dataclass
class PartNum:
    num: int
    adj: bool | None
    location: list[Point]


class GearMap:
    def __init__(self, schematic: str) -> None:
        self.pt_nums: list[PartNum] = []
        self.parts: list[Point] = []
        num: str = ""
        for row, line in enumerate(schematic.strip().split("\n")):
            for col, char in enumerate(line.strip()):
                if char in ascii_nums:
                    num += char
                elif num != "":
                    self.pt_nums.append(
                        PartNum(
                            num=int(num),
                            adj=None,
                            location=[Point(row, col - i - 1) for i in range(len(num))],
                        )
                    )
                    num = ""
                if char != "." and char not in ascii_nums:
                    self.parts.append(Point(row, col))
        # move non part numbers
        for pt_num in list(self.pt_nums):
            pt_num.adj = any(
                [
                    any([pt.adjacent(part) for part in self.parts])
                    for pt in pt_num.location
                ]
            )


def pt1(input: str) -> str:
    map = GearMap(input)
    print(map.pt_nums)
    print(map.parts)
    return sum([p.num for p in map.pt_nums if p.adj])


def pt2(input: str) -> str:
    return input


if __name__ == "__main__":
    with open("day03/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        # print(pt2(input))
