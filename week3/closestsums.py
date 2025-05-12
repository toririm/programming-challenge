import bisect


def get_closest(cur, q, candidate):
    if abs(cur - q) < abs(candidate - q):
        return cur
    else:
        return candidate


def main(n):
    nums = [int(input()) for _ in range(n)]

    sums = set()
    for i in range(n):
        for j in range(i + 1, n):
            sums.add(nums[i] + nums[j])
    sums = sorted(list(sums))

    sum_size = len(sums)

    m = int(input())

    def get_idx(idx):
        if idx > sum_size - 1:
            return sum_size - 1
        elif idx == -1:
            return 0
        else:
            return idx

    for _ in range(m):
        q = int(input())
        idx_l = bisect.bisect_left(sums, q)
        idx_r = bisect.bisect_right(sums, q)
        closest = sums[get_idx(idx_l)]
        closest = get_closest(closest, q, sums[get_idx(idx_l - 1)])
        closest = get_closest(closest, q, sums[get_idx(idx_l + 1)])
        closest = get_closest(closest, q, sums[get_idx(idx_r)])
        closest = get_closest(closest, q, sums[get_idx(idx_r - 1)])
        closest = get_closest(closest, q, sums[get_idx(idx_r + 1)])

        print(f"Closest sum to {q} is {closest}.")


cases = 1
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(f"Case {cases}:")
    main(n)
    cases += 1
