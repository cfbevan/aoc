package main

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
}
