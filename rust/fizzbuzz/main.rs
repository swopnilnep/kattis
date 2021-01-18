use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let nums: Vec<i16> = stdin
        .lock()
        .lines()
        .next()
        .unwrap()
        .unwrap()
        .split_whitespace()
        .map(|n| n.parse().unwrap())
        .collect();
    let x  = nums[0];
    let y  = nums[1];
    let n  = nums[2];
    for i in 1..(n+1) {
        match i {
            i if i % x == 0 && i % y == 0 => println!("FizzBuzz"),
            i if i % x == 0 => println!("Fizz"),
            i if i % y == 0 => println!("Buzz"),
            i => println!("{}", i),
        }
    }
}