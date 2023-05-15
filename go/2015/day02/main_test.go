package main

import (
	"testing"
)

func TestPart1_ex1(t *testing.T) {
	input := "2x3x4"
	expect := 58
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex2(t *testing.T) {
	input := "1x1x10"
	expect := 43
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart2_ex1(t *testing.T) {
	input := "2x3x4"
	expect := 34
	actual := part2(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart2_ex2(t *testing.T) {
	input := "1x1x10"
	expect := 14
	actual := part2(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}
