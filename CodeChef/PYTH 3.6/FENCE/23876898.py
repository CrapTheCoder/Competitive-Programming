for _ in range(int(input())):
    n, m, k = map(int, input().split())

    a = 0

    rs = {}
    cs = {}
    rcs = []

    for __ in range(k):
        r, c = map(int, input().split())

        r -= 1
        c -= 1

        rs[r] = rs.get(r, []) + [c]
        cs[c] = cs.get(c, []) + [r]

        rcs.append((r, c))

    for r, c in rcs:
        if c-1 not in rs[r]: a += 1
        if c+1 not in rs[r]: a += 1
        if r-1 not in cs[c]: a += 1
        if r+1 not in cs[c]: a += 1

    print(a)