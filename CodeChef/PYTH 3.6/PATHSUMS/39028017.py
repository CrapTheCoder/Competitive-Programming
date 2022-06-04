def dfs(u=0, p=-1, i=1):
    color[u] = i

    for v in g[u]:
        if v != p:
            dfs(v, u, 1 if i == 2 else 2)

for _ in range(int(input())):
    n = int(input())
    g = [[] for _ in range(n)]
    color = [0] * n

    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        g[u].append(v)
        g[v].append(u)

    dfs()
    print(*color)
