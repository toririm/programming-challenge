x = int(input())
n = int(input())
spent = [int(input()) for _ in range(n)]

ans = x * (n + 1) - sum(spent)
print(ans)
