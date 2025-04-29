p, t = map(int, input().split())

heard = [[] for _ in range(p)]

while True:
    try:
        line = input()
    except EOFError:
        break
    i, j = map(int, line.split())
    i -= 1
    heard[i].append(j)

opinions = set()

for i in range(p):
    opinions.add(" ".join(map(str, sorted(heard[i]))))

print(len(opinions))
