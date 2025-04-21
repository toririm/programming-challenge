s = input()


def cnt(s, k):
    return int(s[0] != s[1]) + int(s[1] == k) + s[2:].count(k) * 2


def prefered(s):
    return s.count("UD") + s.count("DU")


print(cnt(s, "D"))
print(cnt(s, "U"))
print(prefered(s))
