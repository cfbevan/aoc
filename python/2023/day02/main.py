class Round:
    def __init__(self, line: str) -> None:
        parts = line.split(",")
        cubes = {
            part.strip().split(" ")[1]: int(part.strip().split(" ")[0])
            for part in parts
        }
        self.red = cubes.get("red", 0)
        self.green = cubes.get("green", 0)
        self.blue = cubes.get("blue", 0)


class Game:
    def __init__(self, line: str) -> None:
        l = line.strip().split(":")
        self.id = int(l[0][5:])
        self.rounds = [Round(r) for r in l[1].strip().split(";")]

    @property
    def red(self) -> int:
        """Minimum number of red cubes needed for game.

        Returns:
            int: Red cubes needed.
        """
        return max([r.red for r in self.rounds])

    @property
    def green(self) -> int:
        """Minimum number of green cubes needed for game.

        Returns:
            int: Green cubes needed.
        """
        return max([r.green for r in self.rounds])

    @property
    def blue(self) -> int:
        """Minimum number of blue cubes needed for game.

        Returns:
            int: Blue cubes needed.
        """
        return max([r.blue for r in self.rounds])

    @property
    def power(self) -> int:
        """Get power of game.

        The number or red, green, and blue cubes needed for game
        multiplied together.

        Returns:
            int: Power of the game.
        """
        return self.red * self.green * self.blue

    def valid(self, red: int, green: int, blue: int) -> bool:
        """Check if game is valid.

        Args:
            red (int): Max red cubes/
            green (int): Max green cubes.
            blue (int): MAx blue cubes.

        Returns:
            bool: True if valid, otherwise False.
        """
        return self.red <= red and self.green <= green and self.blue <= blue


def pt1(input: str) -> str:
    games = [Game(l.strip()) for l in input.strip().split("\n")]
    return sum([g.id for g in games if g.valid(12, 13, 14)])


def pt2(input: str) -> str:
    games = [Game(l.strip()) for l in input.strip().split("\n")]
    return sum([g.power for g in games])


if __name__ == "__main__":
    with open("day02/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
