n, m, k = map(int, input().split())
lands = list(map(int, input().split()))
r_houses = list(map(int, input().split()))
s_houses = list(map(int, input().split()))

r22s = [(2 * r) ** 2 for r in r_houses] + [2 * (s**2) for s in s_houses]
r22s.sort()
lands22 = [(2 * r) ** 2 for r in lands]
lands22.sort()

i = 0
j = 0
ans = 0
while i < n and j < m + k:
    if lands22[i] > r22s[j]:
        i += 1
        j += 1
        ans += 1
    else:
        i += 1

print(ans)
