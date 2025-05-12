s = input()

candidates = []

for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        candidates.append(s[:i][::-1] + s[i:j][::-1] + s[j:][::-1])

candidates = sorted(candidates)
print(candidates[0])
