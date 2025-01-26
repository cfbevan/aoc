from .main import Map

test_input = ""
with open("day06/test_input.txt", "r") as fin:
    test_input = fin.read().strip()


map = Map(test_input)

print(str(map))
input()

while map.tick():
    print(str(map))
    input()

print(str(map))
