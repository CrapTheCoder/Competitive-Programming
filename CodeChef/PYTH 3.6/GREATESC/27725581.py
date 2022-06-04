def BFS():
    queue = [s]

    pred = [-1] * n

    visited = [False] * n
    visited[s] = True

    dist = [float('inf')] * n
    dist[s] = 0

    while queue:
        u = queue[0]
        del queue[0]

        for i in range(len(graph[u])):
            if not visited[graph[u][i]]:
                visited[graph[u][i]] = True
                dist[graph[u][i]] = dist[u] + 1
                pred[graph[u][i]] = u

                queue.append(graph[u][i])

                if graph[u][i] == d:
                   return dist[graph[u][i]]

    return 0

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1

    if v != u:
        graph[u].append(v)
        graph[v].append(u)

s, d = map(int, input().split())
s -= 1
d -= 1

print(BFS())