from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 7)

## UTILITY
MOD = 10 ** 9 + 7
MAX = 5 * 10 ** 5 + 13

fct = [0] * MAX
fct[0] = 1

for i in range(1, MAX):
    fct[i] = fct[i-1] * i % MOD


def inv(a):
    return pow(a, MOD - 2, MOD)


## DFS
def count(u, p=-1):
    s = 1

    for v in g[u]:
        if v != p:
            c = count(v, u)
            s += c

    x[u] = s
    return s

def solve(u, r, p=-1):
    if p == -1:
        for v in g[u]:
            solve(v, r, u)

    else:
        r -= 2 * x[u] - 1
        r += x[p] - 1

        c1, c2 = x[u], x[p]
        x[u], x[p] = x[p], x[p] - x[u]

        mini[u-1] = -r, u

        for v in g[u]:
            if v != p:
                solve(v, r, u)

        x[u], x[p] = c1, c2


## MAIN
for _ in range(int(input())):
    n, k = map(int, input().split())

    g = [[] for _ in range(n+5)]

    for _ in range(1, n):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    u = 1
    x = [-1] * (n+1)
    count(u)

    b = sum(x) - len(x)
    mini = [()] * n
    mini[0] = (-b, 1)

    solve(1, b)
    mini.sort()

    count(mini[-k][1])

    f = fct[n-1]
    for i in x[1:]:
        if i != n:
            f = f * inv(i) % MOD

    print(mini[-k][1], f)
