from collections import Counter
from csv import Error
from enum import Enum, auto


class Direction(Enum):
    UP: int = auto()
    RIGHT: int = auto()
    LEFT: int = auto()
    DOWN: int = auto()


class MapItem(Enum):
    EMPTY: int = auto()
    OBSTRUCTION: int = auto()
    GUARD: int = auto()
    BORDER: int = auto()


class Guard:
    def __init__(self, x: int, y: int, direction: Direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn(self):
        match self.direction:
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.RIGHT:
                self.direction = Direction.DOWN
            case Direction.DOWN:
                self.direction = Direction.LEFT
            case Direction.LEFT:
                self.direction = Direction.UP

    def move(self):
        match self.direction:
            case Direction.UP:
                self.x = self.x - 1
            case Direction.RIGHT:
                self.y = self.y + 1
            case Direction.DOWN:
                self.x = self.x + 1
            case Direction.LEFT:
                self.y = self.y - 1

    @property
    def map_item(self) -> str:
        match self.direction:
            case Direction.UP:
                return "^"
            case Direction.RIGHT:
                return ">"
            case Direction.DOWN:
                return "v"
            case Direction.LEFT:
                return "<"


class Map:
    def __init__(self, input: str):
        self.data: list[list[str]] = [[c for c in r] for r in input.split("\n")]
        for x, row in enumerate(self.data):
            for y, val in enumerate(row):
                if val == "^":
                    self.guard = Guard(x, y, Direction.UP)
                elif val == ">":
                    self.guard = Guard(x, y, Direction.RIGHT)
                elif val == "<":
                    self.guard = Guard(x, y, Direction.LEFT)
                elif val == "v":
                    self.guard = Guard(x, y, Direction.DOWN)

    def __str__(self) -> str:
        return "\n".join(["".join(r) for r in self.data])

    def on_map(self, x: int, y: int) -> bool:
        """Return if given coordinate is on map."""
        return x >= 0 and x < len(self.data[0]) and y >= 0 and y < len(self.data)

    def _get(self, x: int, y: int) -> MapItem:
        """Get item on map"""
        if self.on_map(x, y):
            item = self.data[x][y]
            if item in (".", "X"):
                return MapItem.EMPTY
            elif item == "#":
                return MapItem.OBSTRUCTION
            elif item in ("^", ">", "v", "<"):
                return MapItem.GUARD
            else:
                raise Error(f"Unknown item at {x}, {y}: {item}")
        return MapItem.BORDER

    def _set(self, x: int, y: int, item: str) -> None:
        self.data[x][y] = item

    @property
    def in_front(self) -> MapItem:
        """Return what is in front of the guard."""
        match self.guard.direction:
            case Direction.UP:
                return self._get(self.guard.x - 1, self.guard.y)
            case Direction.DOWN:
                return self._get(self.guard.x + 1, self.guard.y)
            case Direction.LEFT:
                return self._get(self.guard.x, self.guard.y - 1)
            case Direction.RIGHT:
                return self._get(self.guard.x, self.guard.y + 1)

    def tick(self) -> bool:
        if self.in_front == MapItem.EMPTY:
            self._set(self.guard.x, self.guard.y, "X")
            self.guard.move()
            self._set(self.guard.x, self.guard.y, self.guard.map_item)
            return True
        if self.in_front == MapItem.OBSTRUCTION:
            self.guard.turn()
            self._set(self.guard.x, self.guard.y, self.guard.map_item)
            return True
        if self.in_front == MapItem.BORDER:
            self._set(self.guard.x, self.guard.y, "X")
        return False

    def traversed_sum(self) -> int:
        return Counter("".join(["".join(r) for r in self.data]))["X"]


def pt1(input: str) -> str:
    map = Map(input)
    while map.tick():
        pass
    return str(map.traversed_sum())


def pt2(input: str) -> str:
    return input


if __name__ == "__main__":
    with open("day06/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        # print(pt2(input))
