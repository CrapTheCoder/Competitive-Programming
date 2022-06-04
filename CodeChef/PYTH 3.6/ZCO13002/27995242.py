def valid(i, j):
    return 0 <= i < n and 0 <= j < n

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

g = [[-float('inf')] * n for _ in range(n)]

for _ in range(m):
    x, y, p = map(int, input().split())
    x -= 1
    y -= 1

    for i in range(p + 1):
        for j in range(p - i + 1):
            if valid(x + i, y + j): g[x + i][y + j] = 0
            if valid(x - i, y + j): g[x - i][y + j] = 0
            if valid(x + i, y - j): g[x + i][y - j] = 0
            if valid(x - i, y - j): g[x - i][y - j] = 0

if g[0][0] != 0:
    print('NO')
    quit()

g[0][0] = a[0][0]

for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            k = float('-inf')

            if valid(i - 1, j) and g[i - 1][j] > k:
                k = g[i - 1][j]

            if valid(i, j - 1) and g[i][j - 1] > k:
                k = g[i][j - 1]

            g[i][j] = k + a[i][j]

if g[n-1][n-1] == float('-inf'):
    print('NO')
else:
    print('YES')
    print(g[-1][-1])
