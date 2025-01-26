fn pt1(s: &str) -> usize {
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
}