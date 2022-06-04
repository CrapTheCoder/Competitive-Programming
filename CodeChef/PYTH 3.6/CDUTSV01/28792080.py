from itertools import combinations

a = list(map(int, input().split()))

p = int(input())

g = [[0] * 8 for _ in range(8)]

for _ in range(p):
    u, v = map(int, input().split())

    u -= 1
    v -= 1

    g[u][v] = g[v][u] = 1

maxi = 0

for i in range(8):
    for j in combinations(list(range(8)), i + 1):
        f = False

        for k in range(i + 1):
            for l in range(k):
                if g[j[k]][j[l]]:
                    f = True
                    break

            if f:
                break

        if not f:
            maxi = max(maxi, sum(a[k] for k in j))

print(maxi)