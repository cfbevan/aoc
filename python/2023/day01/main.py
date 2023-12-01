from re import compile


digit_re = compile(r"\d")


def line_to_digit(line: str) -> int:
    """Takes a string and extracts the first and last digit to form a number.

    Args:
        line (str): Line to parse.

    Returns:
        int: Two digit number.
    """
    digits = digit_re.findall(line)
    return int(f"{digits[0]}{digits[-1]}")


NUM_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

word_re = compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")


def line_to_digit2(line: str) -> int:
    """Takes a string and extracts the first and last digit to form a number.

    This one also handles spelt out digits.

    Args:
        line (str): Line to parse.

    Returns:
        int: Two digit number.
    """
    digits = [NUM_WORDS[match.group(1)] for match in word_re.finditer(line)]
    return int(f"{digits[0]}{digits[-1]}")


def pt1(input: str) -> str:
    return sum([line_to_digit(line) for line in input.split("\n")])


def pt2(input: str) -> str:
    return sum([line_to_digit2(line) for line in input.split("\n")])


if __name__ == "__main__":
    with open("day01/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
