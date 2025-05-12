a, b = map(int, input().split())
up = [tuple(map(int, input().split())) for _ in range(a)]
down = [tuple(map(int, input().split())) for _ in range(b)]

upp = []
pre = 0
t_pre = 0
for i in range(a):
    h, t = up[i]
    upp.append((t_pre, t_pre + t, pre, pre + h))
    pre += h
    t_pre += t

downn = []
t_pre = 0
for i in range(b):
    h, t = down[i]
    downn.append((t_pre, t_pre + t, pre, pre - h))
    pre -= h
    t_pre += t

i = j = 0
while i < len(upp) and j < len(downn):
    t1s, t1e, h1s, h1e = upp[i]
    t2s, t2e, h2s, h2e = downn[j]

    t_start = max(t1s, t2s)
    t_end = min(t1e, t2e)

    if t_start < t_end:
        v1 = (h1e - h1s) / (t1e - t1s)
        b1 = h1s - v1 * t1s

        v2 = (h2e - h2s) / (t2e - t2s)
        b2 = h2s - v2 * t2s

        if v1 != v2:
            t_cross = (b2 - b1) / (v1 - v2)
            if t_start <= t_cross <= t_end:
                print(f"{t_cross:.10f}")
                break

    if t1e < t2e:
        i += 1
    else:
        j += 1
