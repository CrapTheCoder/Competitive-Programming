from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

def dfs(u):
    if visited[u]:
        return False
    visited[u] = True

    if u == y:
        return True

    f = False
    for v in d[u]:
        f = f or dfs(v)
    return f

for _ in range(int(input())):
    n, x, y = input().split()
    x = x.upper().strip()
    y = y.upper().strip()
    n = int(n)

    d = {x: [], y: []}

    g = {x, y}

    for _ in range(n):
        a, b = input().split()
        a = a.upper().strip()
        b = b.upper().strip()

        g.add(a)
        g.add(b)

        d[a] = d.get(a, []) + [b]
        d[b] = d.get(b, []) + [a]

    visited = {i: False for i in g}

    if dfs(x):
        print('Quarantine')
    else:
        print('Stay Home, Stay Safe')
