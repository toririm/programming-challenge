from bisect import bisect_right, insort

n, k = map(int, input().split())
activities = [tuple(map(int, input().split())) for _ in range(n)]
activities.sort(key=lambda x: x[1])

end_times = []

ans = 0
for start, end in activities:
    idx = bisect_right(end_times, start)
    if idx > 0:
        del end_times[idx - 1]
        insort(end_times, end)
        ans += 1
    elif len(end_times) < k:
        insort(end_times, end)
        ans += 1

print(ans)
