from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
l = [list(map(int, input().strip())) for _ in range(n)]

pre = [[0] * m for _ in range(n)]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    x1 -= 1
    y1 -= 1

    x2 -= 1
    y2 -= 1

    pre[x1][y1] += 1
    if x2+1 < n: pre[x2+1][y1] -= 1
    if y2+1 < m: pre[x1][y2+1] -= 1
    if (x2+1 < n) and (y2+1 < m): pre[x2+1][y2+1] += 1

for i in range(1, n):
    for j in range(m):
        pre[i][j] += pre[i-1][j]

for i in range(n):
    for j in range(1, m):
        pre[i][j] += pre[i][j-1]

for i in range(n):
    for j in range(m):
        print((pre[i][j] + l[i][j]) % 2, end='')

    print()