n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

p = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + a[i-1][j-1]

s = 0

for _ in range(int(input())):
    l = list(input().split())
    x1, y1, x2, y2 = map(int, l[:4])
    pb = float(l[-1])

    s += (p[x2][y2] - p[x1-1][y2] - p[x2][y1-1] + p[x1-1][y1-1]) * pb

print(s)
