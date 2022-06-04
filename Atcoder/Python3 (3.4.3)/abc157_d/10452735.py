from sys import setrecursionlimit
setrecursionlimit(2 * 10 ** 9)

n, m, k = map(int, input().split())

def dfs(u):
    if visited[u]:
        return

    visited[u] = True

    for v in graph[u]:
        s.add(v)
        dfs(v)

graph = {i: set() for i in range(n)}
blocks = {i: set() for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].add(b)
    graph[b].add(a)

for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    blocks[c].add(d)
    blocks[d].add(c)

ans = [0] * n

visited = [False] * n

for u in range(n):
    if not visited[u]:
        s = set()

        dfs(u)

        l = len(s)

        for i in s:
            ans[i] += l - 1
            ans[i] -= len(blocks[i].intersection(s))
            ans[i] -= len(graph[i].intersection(s))

print(*ans)