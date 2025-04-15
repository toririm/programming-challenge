n = int(input())
ans = 0

for i in range(n):
    q, y = map(float, input().split())
    ans += q * y

print("{:.3f}".format(ans))
