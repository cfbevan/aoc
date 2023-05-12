#!/bin/bash

year=${PWD##*/}
day=${1##+(0)}
project=$(printf "day%02d" $1)
session="$AOC_SESSION"

mkdir ${project}

cd ${project}

# init go mod
go mod init "aoc/${year}/${day}"

# get input
curl -s "https://adventofcode.com/${year}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

# add readme
touch README.md

echo -n 'package main

import (
    "fmt"
    "os"
)

func part1(input string) string {
    return input
}

func part2(input string) string {
    return input
}

func main() {
    b, err := os.ReadFile("input.txt")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

    str := string(b)

    fmt.Println(part1(str))
    fmt.Println(part2(str))
}' > main.go

echo -n 'package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	input := ""
	expect := ""
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart2(t *testing.T) {
	input := ""
	expect := ""
	actual := part2(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}' > main_test.go