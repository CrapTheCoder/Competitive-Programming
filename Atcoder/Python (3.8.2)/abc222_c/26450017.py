n, m = map(int, input().split())
a = [input().strip() for _ in range(2*n)]

c = [[0, i] for i in range(1, 2*n+1)]

for j in range(m):
    for i in range(n):
        x = c[2*i][1] - 1
        y = c[2*i+1][1] - 1

        if a[x][j] == 'G' and a[y][j] == 'C': c[2*i][0] += 1
        if a[x][j] == 'G' and a[y][j] == 'P': c[2*i+1][0] += 1
        if a[x][j] == 'C' and a[y][j] == 'G': c[2*i+1][0] += 1
        if a[x][j] == 'C' and a[y][j] == 'P': c[2*i][0] += 1
        if a[x][j] == 'P' and a[y][j] == 'G': c[2*i][0] += 1
        if a[x][j] == 'P' and a[y][j] == 'C': c[2*i+1][0] += 1

    c.sort(key=lambda x: x[1])
    c.sort(key=lambda x: -x[0])

for i in c:
    print(i[1])
