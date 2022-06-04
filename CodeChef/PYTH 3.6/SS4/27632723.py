def bfs():
    q = [[0, -1, 0]]

    while q:
        new = []

        for i in q:
            u, p, l = i

            for v in g[u]:
                if v != p:
                    lvls[v] = l + 1
                    new.append([v, u, l + 1])

        q = new

n = int(input())
g = [[] for i in range(n)]

if n == 1:
    print(1)
else:
    lvls = [0] * n
    lvls[0] = 0

    for _ in range(n - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1

        g[x].append(y)
        g[y].append(x)


    bfs()

    cnts = [0] * n

    for i in lvls:
        cnts[i] += 1

    print(cnts.index(max(cnts)) + 1)
