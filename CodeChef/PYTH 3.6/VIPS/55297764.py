from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

P = -123123123

def solve(u=0, p=P):
    if len(g[u]) == 1:
        if a[u] == 0:
            return float('inf'), 1

        return a[u], 1

    s = l = 0
    for v in g[u]:
        if v != p:
            x, y = solve(v, u)
            s += x
            l += y

    if a[u] == 0:
        return s, l

    return min(s, a[u] * l), l

for _ in range(int(input())):
    n = int(input())

    g = [[] for _ in range(n)]
    g[0].append(P)

    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)

    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        continue

    print(solve()[0])
