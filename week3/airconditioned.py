n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

intervals.sort(key=lambda x: x[1])

ans = 0
used = [False] * n

i = 0
while i < n:
    if used[i]:
        i += 1
        continue

    temp = intervals[i][1]
    ans += 1

    for j in range(i, n):
        if intervals[j][0] <= temp <= intervals[j][1]:
            used[j] = True
    i += 1

print(ans)
