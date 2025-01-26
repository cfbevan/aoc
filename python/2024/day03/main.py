from re import compile

mul_regex = compile(r"mul\((\d+),(\d+)\)")
mul_do_dont_regex = compile(r"(?P<op>do|don\'t|mul)\(((?P<x>\d+),(?P<y>\d+))?\)")


def pt1(input: str) -> str:
    return str(
        sum(
            int(match.groups()[0]) * int(match.groups()[1])
            for line in input.split("\n")
            for match in mul_regex.finditer(line)
        )
    )


def pt2(input: str) -> str:
    enabled = True
    total = 0
    for line in input.split("\n"):
        for match in mul_do_dont_regex.finditer(line):
            match match.groupdict()["op"]:
                case "do":
                    enabled = True
                case "don't":
                    enabled = False
                case "mul":
                    if enabled:
                        total = total + (
                            int(match.groupdict()["x"]) * int(match.groupdict()["y"])
                        )
                case _:
                    print(f"Error: {match.groupdict()}")
    return str(total)


if __name__ == "__main__":
    with open("day03/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
