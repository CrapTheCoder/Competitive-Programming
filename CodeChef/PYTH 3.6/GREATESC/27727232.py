def bfs():
    queue = [root]

    visited = [0] * n
    visited[root] = 1

    dis = [float('inf')] * n
    dis[root] = 0

    while queue:
        vertex = queue[0]
        queue = queue[1:]

        for i in range(len(graph[vertex])):
            if not visited[graph[vertex][i]]:
                visited[graph[vertex][i]] = 1
                dis[graph[vertex][i]] = dis[vertex] + 1

                queue.append(graph[vertex][i])

                if graph[vertex][i] == reach:
                    return dis[graph[vertex][i]]

    return 0

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)

root, reach = map(int, input().split())
root -= 1
reach -= 1

print(bfs())
