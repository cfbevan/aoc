package com.github.cfbevan.aoc;

import org.apache.commons.io.IOUtils;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        try (FileInputStream inputStream = new FileInputStream("input.txt")) {
            // Read input file and convert to string
            String everything = IOUtils.toString(inputStream, "UTF-8");
            // Call part1 and part2
            System.out.printf("Part 1: %s%n", part1(everything));
            System.out.printf("Part 2: %s%n", part2(everything));
        }
    }

    public static int part1(String input) {
        /**
         * Determine final floor after reading input
         * where '(' means up one floor and ')' means down one floor
         * 
         * @param input input string
         */
        int floor = 0;
        for (int i = 0; i < input.length(); i++) {
            switch (input.charAt(i)) {
                case '(':
                    floor++;
                    break;
                case ')':
                    floor--;
                    break;
                default:
                    break;
            }
        }
        return floor;
    }

    public static int part2(String input) {
        /**
         * Determine position of first character that causes Santa to enter the basement
         * where '(' means up one floor and ')' means down one floor
         * 
         * @param input input string
         */
        int floor = 0;
        for (int i = 0; i < input.length(); i++) {
            switch (input.charAt(i)) {
                case '(':
                    floor++;
                    break;
                case ')':
                    floor--;
                    break;
                default:
                    break;
            }
            if (floor == -1) {
                return i + 1;
            }
        }
        return -1;
    }
}