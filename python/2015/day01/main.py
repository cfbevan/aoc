from collections import Counter


def pt1(input: str) -> int:
    c = Counter(input)
    return c["("] - c[")"]


def pt2(input: str) -> int:
    floor = 0
    for i, c in enumerate(input):
        match c:
            case "(":
                floor = floor + 1
            case ")":
                floor = floor - 1
        if floor < 0:
            return i + 1
    return -1


if __name__ == "__main__":
    with open("day01/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
