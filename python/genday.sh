#!/bin/bash

year=${PWD##*/}
day=${1##+(0)}
project=$(printf "day%02d" $1)
session="$AOC_SESSION"

mkdir ${project}

cd ${project}

# get input
curl -s "https://adventofcode.com/${year}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

# add readme
touch README.md
touch __init__.py
touch test_input.txt

echo -n "def pt1(input: str) -> str:
    return input

def pt2(input: str) -> str:
    return input

if __name__ == '__main__':
    with open('${project}/input.txt', 'r') as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
" > main.py

echo -n "from unittest import TestCase
from unittest import main

from .main import pt1
from .main import pt2

input = ''
with open('${project}/test_input.txt', 'r') as fin:
    input = fin.read().strip()

class Test${project}(TestCase):

    def test_pt1(self):
        output = pt1(input)
        expected = input
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = input
        self.assertEqual(output, expected)
        
if __name__ == '__main__':
    main()" > test.py