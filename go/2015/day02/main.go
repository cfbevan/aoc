package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func part1(input string) int {
	total := 0
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		lwh := strings.Split(line, "x")
		if len(lwh) == 3 {
			l, _ := strconv.Atoi(lwh[0])
			w, _ := strconv.Atoi(lwh[1])
			h, _ := strconv.Atoi(lwh[2])
			sizes := []int{2 * l * w, 2 * w * h, 2 * h * l}
			sort.Slice(
				sizes,
				func(i, j int) bool {
					return sizes[i] < sizes[j]
				},
			)
			for _, v := range sizes {
				total += v
			}
			total += sizes[0] / 2
		}
	}
	return total
}

func part2(input string) int {
	total := 0
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		lwh := strings.Split(line, "x")
		if len(lwh) == 3 {
			l, _ := strconv.Atoi(lwh[0])
			w, _ := strconv.Atoi(lwh[1])
			h, _ := strconv.Atoi(lwh[2])
			sizes := []int{l, w, h}
			sort.Slice(
				sizes,
				func(i, j int) bool {
					return sizes[i] < sizes[j]
				},
			)
			total += (l * w * h) + sizes[0] + sizes[1] + sizes[0] + sizes[1]
		}
	}
	return total
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
