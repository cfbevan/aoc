def parse_reports(input: str) -> list[list[int]]:
    """Parse input string into a list of lists of

    Args:
        input (str): Data of reports.

    Returns:
        list[list[int]]: Parsed reports.
    """
    return [[int(x) for x in line.split()] for line in input.split("\n")]


def safe(report: list[int]) -> bool:
    """Check if a report is safe.

    So, a report only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    Args:
        report (list[int]): Report to check.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    return all(
        report[i] - report[i - 1] in [1, 2, 3] for i in range(1, len(report))
    ) or all(report[i] - report[i - 1] in [-1, -2, -3] for i in range(1, len(report)))


def pt1(input: str) -> str:
    return str(sum(safe(report) for report in parse_reports(input)))


def safe2(report: list[int]) -> bool:
    """Check if a report is safe.

    So, a report only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    The Problem Dampener is a reactor-mounted module that lets the reactor
    safety systems tolerate a single bad level in what would otherwise be
    a safe report. It's like the bad level never happened!

    Args:
        report (list[int]): Report to check.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    return any(safe(report[:i] + report[i + 1 :]) for i in range(len(report)))


def pt2(input: str) -> str:
    return str(sum(safe2(report) for report in parse_reports(input)))


if __name__ == "__main__":
    with open("day02/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
