use std::io;
use std::io::prelude::*;

fn main() {
    let stdin = io::stdin();
    let mut sum = 0;
    let mut count = 0;
    for line in stdin.lock().lines() {
        sum += line.unwrap().chars().count();
        count += 1;
    }
    println!("Average line length: {}", sum as f64 / count as f64)
}
