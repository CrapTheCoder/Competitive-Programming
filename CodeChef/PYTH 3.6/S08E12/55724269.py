INF = float('inf')


def count(s, t):
    s = s.copy()
    t = t.copy()

    if len(s) != len(t):
        return INF

    n = len(s)

    c = 0
    for i in range(n):
        if s[i] != t[i]:
            if i+1 >= n:
                return INF

            c += 1
            s[i] ^= 1
            s[i+1] ^= 1

    return c


def solve(s, t, beg, end):
    s = s.copy()
    t = t.copy()

    tot = beg + end

    t = t[beg:]
    if end != 0:
        t = t[:-end]

    if beg == end == 0:
        return count(s, t) + tot

    elif end == 0:
        c1 = count(s, t)

        s[0] ^= 1
        c2 = count(s, t) + 1

        return min(c1, c2) + tot

    elif beg == 0:
        c1 = count(s, t)

        s[-1] ^= 1
        c2 = count(s, t) + 1

        return min(c1, c2) + tot

    else:
        c1 = count(s, t)  # 0 0

        s[0] ^= 1
        c2 = count(s, t) + 1  # 1 0

        s[-1] ^= 1
        c3 = count(s, t) + 2  # 1 1

        s[0] ^= 1
        c4 = count(s, t) + 1  # 0 1

        return min(c1, c2, c3, c4) + tot

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = list(map(int, input().strip()))
    t = list(map(int, input().strip()))

    if n > m:
        print(-1)
        continue

    elif m == n:
        x = solve(s, t, 0, 0)
        print(x if x != INF else -1)

    else:
        tot = m - n
        mini = INF

        for i in range(tot+1):
            mini = min(mini, solve(s, t, i, tot-i))

        if mini == INF:
            print(-1)
        else:
            print(mini)
