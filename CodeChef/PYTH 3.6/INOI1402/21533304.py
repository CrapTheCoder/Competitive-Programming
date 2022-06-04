def FloydWarshall():
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if g[u][k] == -1 or g[k][v] == -1 or u == v:
                    continue
                if g[u][v] == -1:
                    g[u][v] = g[u][k] + g[k][v]
                else:
                    g[u][v] = min(g[u][v], g[u][k] + g[k][v])

n, f = map(int, input().split())
g = [[-1] * n for _ in range(n)]

for _ in range(f):
    a, b, c  = map(int, input().split())
    g[a-1][b-1] = c
    g[b-1][a-1] = c

FloydWarshall()
print(max(max(i) for i in g))
