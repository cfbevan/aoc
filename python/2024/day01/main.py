from collections import Counter

def distance(x: int, y: int) -> int:
    """Calculates the absolute difference between two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The absolute difference between x and y.
    """
    return abs(x - y)

def make_lists(input: str) -> tuple[list[int], list[int]]:
    """Reads input and returns two lists of integers.

    Args:
        input (str): Input string with two numbers per line separated by 3 spaces.

    Returns:
        tuple[list[int], list[int]]: Two lists of integers.
    """
    list1 = []
    list2 = []
    for line in input.split('\n'):
        a, b = line.split('   ')  # 3 spaces between numbers
        list1.append(int(a))
        list2.append(int(b))
    return list1, list2

def pt1(input: str) -> str:
    # read each line of input
    list1, list2 = make_lists(input)
    # sort lists
    list1 = sorted(list1)
    list2 = sorted(list2)
    # sum distances between sorted lists
    return str(sum([distance(x, y) for x, y in zip(list1, list2)]))

def pt2(input: str) -> str:
    # read each line of input
    list1, list2 = make_lists(input)
    counts = Counter(list2)
    return str(sum([counts.get(x, 0) * x for x in list1]))

if __name__ == '__main__':
    with open('day01/input.txt', 'r') as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
