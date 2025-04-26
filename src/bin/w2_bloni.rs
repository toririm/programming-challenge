use std::collections::HashMap;
use std::io;

fn main() {
    let stdin = io::read_to_string(io::stdin()).unwrap();
    let _n = stdin.lines().next().unwrap().parse::<usize>().unwrap();
    let h: Vec<usize> = stdin
        .lines()
        .nth(1)
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse::<usize>().unwrap())
        .collect();
    let mut map: HashMap<usize, usize> = HashMap::new();
    for a in h {
        if *map.get(&a).unwrap_or(&0) > 0 {
            *map.get_mut(&a).unwrap() -= 1;
        }
        *map.entry(a - 1).or_insert(0) += 1;
    }
    let ans: usize = map.values().sum();
    println!("{}", ans);
}
