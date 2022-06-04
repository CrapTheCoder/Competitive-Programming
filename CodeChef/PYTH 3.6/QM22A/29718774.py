def dfs(u=0):
    if visited[u]:
        return

    visited[u] = True

    for v in range(n):
        if g[u][v]:
            dfs(v)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

c = 0

for u in range(n):
    if not visited[u]:
        dfs(u)

        c += 1

print(c)