n, h = map(int, input().split())
obs = [0] * (h + 2)

for i in range(n):
    if i % 2 == 0:
        level = h + 1 - int(input())
        obs[level] += 1
        obs[h + 1] -= 1
    else:
        level = int(input())
        obs[1] += 1
        obs[level + 1] -= 1

for i in range(1, h + 1):
    obs[i] += obs[i - 1]

min_obs = min(obs[1 : h + 1])
min_idx = obs[1 : h + 1].index(min_obs) + 1

print(min_obs, obs[1 : h + 1].count(min_obs))
