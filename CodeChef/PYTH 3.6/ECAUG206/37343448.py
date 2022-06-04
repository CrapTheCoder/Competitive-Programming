def dfs(u):
    if visited[u]:
        return

    visited[u] = True

    for v in graph[u]:
        dfs(v)

for _ in range(int(input())):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    t = 0

    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i)
            t += 1

    print(t)