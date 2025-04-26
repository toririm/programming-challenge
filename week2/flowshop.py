n, m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

available_time = [0] * m
finish_time = [0] * n

for i in range(n):
    current_time = 0
    for j in range(m):
        start_time = max(current_time, available_time[j])
        finish = start_time + p[i][j]
        available_time[j] = finish
        current_time = finish
    finish_time[i] = current_time

print(*finish_time)
