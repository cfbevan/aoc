#!/bin/bash

year=${PWD##*/}
day=${1##+(0)}
project=$(printf "day%02d" $1)
session="$AOC_SESSION"

cargo new ${project}

cd ${project}

# get input
curl -s "https://adventofcode.com/${year}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

# add readme
touch README.md

echo -n 'fn pt1(s: &str) -> usize {
    return s;
}

fn pt2(s: &str) -> usize {
    return s;
}

fn main() {
    let data = include_str!("../input.txt").trim();
    println!(
        "Part 1: {}",
        pt1(data)
    );

    println!(
        "Part 2: {}",
        pt2(data)
    );
}

#[cfg(test)]
mod tests {
    
    #[test]
    fn pt1_ex1() {
        let test = "";
        assert_eq!(pt1(test), 0)
    }
}' > src/main.rs
