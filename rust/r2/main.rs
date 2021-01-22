use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let nums:Vec<i16> = stdin
        // Locks the handle to the standard input stream
        // returning a readable guard. The lock is released
        // when the returned lock goes out of scope. 
        .lock()
        // Returns an iterator over the lines of the reader
        .lines()
        // Advances the iterator and returns the next value
        .next()
        .unwrap()
        .unwrap()
        .split_whitespace()
        .map(|n| n.parse().unwrap())
        .collect()
        ;
    println!("{}", nums[1] * 2 - nums[0]);
}
