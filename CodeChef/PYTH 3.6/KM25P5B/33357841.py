def dfs(u, s):
    if visited[u]:
        return 'z' * 100

    visited[u] = 1

    minis = []

    for v, x in enumerate(g[u]):
        if x == 0:
            continue

        d = dfs(v, s+a[v])
        minis.append(d)

    if minis:
        return min(minis)

    return s

n = int(input())
a = input().split()

visited = [0] * n
g = [list(map(int, input().split())) for _ in range(n)]

print(dfs(0, a[0]))