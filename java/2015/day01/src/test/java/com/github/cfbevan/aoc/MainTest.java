package com.github.cfbevan.aoc;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MainTest {

    @Test
    public void testPart1() {
        String input = "()()";
        assertEquals(0, Main.part1(input));
        input = "()()";
        assertEquals(0, Main.part1(input));
        input = "(((";
        assertEquals(3, Main.part1(input));
        input = "(()(()(";
        assertEquals(3, Main.part1(input));
        input = "))(((((";
        assertEquals(3, Main.part1(input));
        input = "())";
        assertEquals(-1, Main.part1(input));
        input = "))(";
        assertEquals(-1, Main.part1(input));
        input = ")))";
        assertEquals(-3, Main.part1(input));
        input = ")())())";
        assertEquals(-3, Main.part1(input));
    }

    @Test
    public void testPart2() {
        String input = ")";
        assertEquals(1, Main.part2(input));
        input = "()())";
        assertEquals(5, Main.part2(input));
    }
}
