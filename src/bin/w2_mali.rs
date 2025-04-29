fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut lines = stdin.lines();
    let n = lines.next().unwrap().parse::<usize>().unwrap();

    let (a_list, b_list): (Vec<usize>, Vec<usize>) = {
        let mut a = vec![];
        let mut b = vec![];
        for _ in 0..n {
            let line = lines.next().unwrap();
            let (x, y) = line.split_once(' ').unwrap();
            a.push(x.parse::<usize>().unwrap());
            b.push(y.parse::<usize>().unwrap());
        }
        (a, b)
    };

    let mut a_counter = [0usize; 101];
    let mut b_counter = [0usize; 101];

    for i in 0..n {
        let a = a_list[i];
        let b = b_list[i];

        a_counter[a] += 1;
        b_counter[b] += 1;

        let mut max_sum = 0;
        let mut a_pointer = 1;
        let mut b_pointer = 100;

        let mut a_cnt = a_counter.clone();
        let mut b_cnt = b_counter.clone();

        while a_pointer <= 100 && b_pointer >= 1 {
            if a_cnt[a_pointer] == 0 {
                a_pointer += 1;
                continue;
            }
            if b_cnt[b_pointer] == 0 {
                b_pointer -= 1;
                continue;
            }
            let consume = a_cnt[a_pointer].min(b_cnt[b_pointer]);
            a_cnt[a_pointer] -= consume;
            b_cnt[b_pointer] -= consume;
            max_sum = max_sum.max(a_pointer + b_pointer);
        }

        println!("{}", max_sum);
    }
}
