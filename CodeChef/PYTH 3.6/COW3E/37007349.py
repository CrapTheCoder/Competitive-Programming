n, m, u, q = map(int, input().split())

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

pre = [[0] * m for _ in range(n)]

for _ in range(u):
    k, x1, y1, x2, y2 = map(int, input().split())

    pre[x1][y1] += k

    if x2+1 < n: pre[x2+1][y1] -= k
    if y2+1 < m: pre[x1][y2+1] -= k
    if x2+1 < n and y2+1 < m: pre[x2+1][y2+1] += k

for i in range(1, n):
    for j in range(m):
        pre[i][j] += pre[i-1][j]

for i in range(n):
    for j in range(1, m):
        pre[i][j] += pre[i][j-1]

for i in range(n):
    for j in range(m):
        pre[i][j] += l[i][j]

for i in range(1, n):
    for j in range(m):
        pre[i][j] += pre[i-1][j]

for i in range(n):
    for j in range(1, m):
        pre[i][j] += pre[i][j-1]

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())

    res = pre[x2][y2]

    if 0 < x1: res -= pre[x1 - 1][y2]
    if 0 < y1: res -= pre[x2][y1 - 1]
    if 0 < x1 and 0 < y1: res += pre[x1 - 1][y1 - 1]

    print(res)
