package main

import (
	"testing"
)

func TestPart1_ex1(t *testing.T) {
	input := "(())"
	expect := 0
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex2(t *testing.T) {
	input := "()()"
	expect := 0
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex3(t *testing.T) {
	input := "((("
	expect := 3
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex4(t *testing.T) {
	input := "(()(()("
	expect := 3
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex5(t *testing.T) {
	input := "))((((("
	expect := 3
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex6(t *testing.T) {
	input := "())"
	expect := -1
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex7(t *testing.T) {
	input := "))("
	expect := -1
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex8(t *testing.T) {
	input := ")))"
	expect := -3
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart1_ex9(t *testing.T) {
	input := ")())())"
	expect := -3
	actual := part1(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart2_ex1(t *testing.T) {
	input := ")"
	expect := 1
	actual := part2(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}

func TestPart2_ex2(t *testing.T) {
	input := "()())"
	expect := 5
	actual := part2(input)
	if expect != actual {
		t.Fatalf(`Test1 failed. got %v, expected %v`, actual, expect)
	}
}
