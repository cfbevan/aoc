package main

import (
	"fmt"
	"os"
)

func part1(input string) int {
	floor := 0

	for _, c := range input {
		if c == '(' {
			floor += 1
		} else if c == ')' {
			floor -= 1
		}
	}
	return floor
}

func part2(input string) int {
	floor := 0
	for i, c := range input {
		if c == '(' {
			floor += 1
		} else if c == ')' {
			floor -= 1
		}
		if floor < 0 {
			return i + 1
		}
	}
	return 0
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
}
