n, m, u, q = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

pre = [[0] * m for _ in range(n)]

for _ in range(u):
    k, r1, c1, r2, c2 = map(int, input().split())

    pre[r1][c1] += k

    if r2+1 < n: pre[r2+1][c1] -= k
    if c2+1 < m: pre[r1][c2+1] -= k
    if r2+1 < n and c2+1 < m: pre[r2+1][c2+1] += k

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
    r1, c1, r2, c2 = map(int, input().split())

    x = pre[r2][c2]

    if r1 - 1 >= 0: x -= pre[r1-1][c2]
    if c1 - 1 >= 0: x -= pre[r2][c1-1]
    if r1 - 1 >= 0 and c1 - 1 >= 0: x += pre[r1-1][c1-1]

    print(x)