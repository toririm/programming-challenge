n = int(input())
while n != 0:
    names = [input() for _ in range(n)]
    names.sort(key=lambda x: x[:2])
    print("\n".join(names))
    print()
    n = int(input())
