n = int(input())
a = list(map(int, input().split()))

ans = dict()

for aa in a:
    if ans.get(aa, 0) > 0:
        ans[aa - 1] = ans.get(aa - 1, 0) + 1
        ans[aa] -= 1
    else:
        ans[aa - 1] = ans.get(aa - 1, 0) + 1

print(sum(ans[aa] for aa in ans))
