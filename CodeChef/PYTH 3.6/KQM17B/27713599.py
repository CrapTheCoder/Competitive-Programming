def track(i, j):
    if x[i][j] == 1 or a[i][j] == '#':
        return

    if a[i][j] == 'K':
        c[0] -= 1

    x[i][j] = 1

    if i + 1 < n: track(i + 1, j)
    if i - 1 >= 0: track(i - 1, j)

    if j + 1 < m: track(i, j + 1)
    if j - 1 >= 0: track(i, j - 1)

n, m = map(int, input().split())
a = [input() for __ in range(n)]

c = [sum(j == 'K' for i in a for j in i)]

x = [[0] * m for __ in range(n)]

d, e = -1, -1

for i in range(n):
    f = 0

    for j in range(m):
        if a[i][j] == 'X':
            d, e = i, j
            f = 1
            break

    if f:
        break

track(d, e)

print('Yes' if c[0] == 0 else 'No')