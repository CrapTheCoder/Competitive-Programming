def solve(u=0, p=-1):
    s = a[u]

    for v in g[u]:
        if v != p:
            s += solve(v, u)

    val[u] = s
    return s

for _ in range(int(input())):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    g = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        g[u].append(v)
        g[v].append(u)

    val = [0] * n
    solve()

    val.sort()

    print(max(0, x - sum(val[:k])))