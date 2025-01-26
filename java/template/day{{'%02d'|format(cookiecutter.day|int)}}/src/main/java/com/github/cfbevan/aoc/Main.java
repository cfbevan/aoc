package com.github.cfbevan.aoc;

import org.apache.commons.io.IOUtils;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        try (FileInputStream inputStream = new FileInputStream("input.txt")) {
            String everything = IOUtils.toString(inputStream, "UTF-8");
            // do something with everything string
            System.out.printf("Part 1: %s%n", part1(everything));
            System.out.printf("Part 2: %s%n", part2(everything));
        }
    }

    public static int part1(String input) {
        // implement part 1
        return 0;
    }

    public static int part2(String input) {
        // implement part 2
        return 0;
    }
}