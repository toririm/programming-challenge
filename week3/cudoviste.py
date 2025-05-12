r, c = map(int, input().split())

parking = [list(input()) for _ in range(r)]

ans = [0] * 5


def is_car(row, col):
    return parking[row][col] == "X"


def is_parkable(row, col):
    return parking[row][col] != "#"


for row in range(r - 1):
    for col in range(c - 1):
        need_to_crush = (
            is_car(row, col)
            + is_car(row, col + 1)
            + is_car(row + 1, col)
            + is_car(row + 1, col + 1)
        )
        parkable = (
            is_parkable(row, col)
            and is_parkable(row, col + 1)
            and is_parkable(row + 1, col)
            and is_parkable(row + 1, col + 1)
        )
        if parkable:
            ans[need_to_crush] += 1

for i in range(5):
    print(ans[i])
