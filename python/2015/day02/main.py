class Box:
    def __init__(self, input: str) -> None:
        self.l, self.w, self.h = [int(x) for x in input.split("x")]

    def wrapping_paper(self) -> int:
        """Calculate wrapping paper needed.

        Surface area of box plus extra equal to the area of smallest side.

        Returns:
            int: Needed paper in square feet.
        """
        sides = [self.l * self.w, self.w * self.h, self.h * self.l]
        return 2 * sides[0] + 2 * sides[1] + 2 * sides[2] + min(sides)

    def ribbon(self) -> int:
        """Calculate ribbon needed.

        Shortest distance around the sides plus the volume of the box.

        Returns:
            int: Needed ribbon in feet.
        """
        sizes = sorted([self.l, self.w, self.h])
        vol = self.l * self.w * self.h
        return sizes[0] + sizes[0] + sizes[1] + sizes[1] + vol


def pt1(input: str) -> int:
    return sum([Box(box).wrapping_paper() for box in input.split("\n")])


def pt2(input: str) -> str:
    return sum([Box(box).ribbon() for box in input.split("\n")])


if __name__ == "__main__":
    with open("day02/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
