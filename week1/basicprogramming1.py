n, t = map(int, input().split())
a = list(map(int, input().split()))


def t2(a):
    if a[0] > a[1]:
        return "Bigger"
    elif a[0] < a[1]:
        return "Smaller"
    else:
        return "Equal"


def t3(a):
    l = a[:3]
    l.sort()
    return l[1]


def t7(a):
    i = 0
    visited = set()
    while True:
        if i >= len(a):
            print("Out")
            return
        if i == len(a) - 1:
            print("Done")
            return
        if i in visited:
            print("Cyclic")
            return
        visited.add(i)
        i = a[i]


match t:
    case 1:
        print(7)
    case 2:
        print(t2(a))
    case 3:
        print(t3(a))
    case 4:
        print(sum(a))
    case 5:
        print(sum(aa for aa in a if aa % 2 == 0))
    case 6:
        print("".join(chr(aa % 26 + ord("a")) for aa in a))
    case 7:
        t7(a)
