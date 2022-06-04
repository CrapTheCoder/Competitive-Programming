from queue import Queue

def bfs(u):
    q = Queue()
    cur = (u, 0)
    q.put(cur)

    visited = [False] * n

    while not q.empty():
        cur = q.get()
        u, w = cur

        if visited[u]:
            continue
        visited[u] = True

        for v in g[u]:
            q.put((v, w+1))

    return cur

n, k = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    g[u].append(v)
    g[v].append(u)

x = bfs(bfs(0)[0])[1]

if x <= k:
    print(0)
else:
    print(x - k)