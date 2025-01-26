package main

import (
	"testing"
)

func TestPart1_ex1(t *testing.T) {
	input := ""
	expect := 0
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart2_ex1(t *testing.T) {
	input := ""
	expect := 1
	actual := part2(input)
	if expect != actual {
		t.Fatalf(`Test failed. got %v, expected %v`, actual, expect)
	}
}
