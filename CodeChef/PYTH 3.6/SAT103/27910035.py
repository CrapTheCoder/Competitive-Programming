for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [[i * j for j in range(1, n+1)] for i in range(1, n+1)]
    dsu = [-1] * n

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        l[u][v] = 0

        while dsu[u] >= 0: u = dsu[u]
        while dsu[v] >= 0: v = dsu[v]

        if u != v:
            if u > v:
                u, v = v, u

            dsu[u] += dsu[v]
            dsu[v] = u

    edges = sorted((l[i][j], i, j) for i in range(n) for j in range(n) if l[i][j])

    c = 0

    for w, u, v in edges:
        while dsu[u] >= 0: u = dsu[u]
        while dsu[v] >= 0: v = dsu[v]

        if u != v:
            if u > v:
                u, v = v, u

            dsu[u] += dsu[v]
            dsu[v] = u

            c += w

    print(c)