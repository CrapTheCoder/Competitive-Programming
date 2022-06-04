from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

size = 0

def dfs(u):
    global size

    if visited[u]:
        return

    size += 1
    visited[u] = True

    for v in g[u]:
        dfs(v)

for _ in range(int(input())):
    n = int(input())
    m = int(input())

    g = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        g[u].append(v)
        g[v].append(u)

    visited = [0] * n

    ans = []

    for u in range(n):
        if not visited[u]:
            dfs(u)
            ans.append(size)
            size = 0

    print(len(ans))
    print(*sorted(ans))