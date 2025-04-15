n1 = int(input())
n2 = int(input())

ans = [n2 - n1, (n2 - 360) - n1, n2 - (n1 - 360)]

ans = list(map(lambda x: -x if x == -180 else x, ans))

minimum = min(ans, key=abs)
for a in ans:
    if abs(a) == abs(minimum):
        print(a)
        break
