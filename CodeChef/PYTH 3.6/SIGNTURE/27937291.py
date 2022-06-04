for _ in range(int(input())):
    n, m = map(int, input().split())

    o = [list(map(int, input())) for r in range(n)]
    c = [list(map(int, input())) for r in range(n)]

    oe = {(i, j) for i in range(n) for j in range(m) if o[i][j]}

    x, y = n + 1, m + 1

    d = [[0] * (m + 2 * y) for i in range(x)] + \
        [[0] * y + c[i] + [0] * y for i in range(n)] + \
        [[0] * (m + 2 * y) for i in range(x)]

    mini = float('inf')


    for i in range(x + n):
        for j in range(y + m):
            g = [d[k][j:j + m] for k in range(i, i + n)]

            try:
                e = {(r, s) for r in range(n) for s in range(m) if g[r][s]}
            except:
                pass

            mini = min(mini, len((e.union(oe)).difference(e.intersection(oe))))

    print(mini)
