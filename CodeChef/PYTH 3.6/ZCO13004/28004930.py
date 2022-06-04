n, m, k = map(int, input().split())

ls = [[1 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r, c, s, f = map(int, input().split())

    r -= 1
    c -= 1

    ls[r][c] = 0

    for i in range(n):
        x = (i + c) - (s + abs(i - r))

        if x >= 0 and not x % f:
            ls[i][c] = 0

    for j in range(m):
        x = (r + j) - (s + abs(j - c))

        if x >= 0 and not x % f:
            ls[r][j] = 0

if not ls[-1][-1] or not ls[0][0]:
    print('NO')
else:
    for i in range(1, n):
        ls[i][0] = ls[i - 1][0]
    for j in range(1, m):
        ls[0][j] = ls[0][j - 1]

    for i in range(1, n):
        for j in range(1, m):
            if not ls[i][j]:
                continue

            ls[i][j] = ls[i - 1][j] or ls[i][j - 1]

    if ls[-1][-1]:
        print('YES')
        print(n + m - 2)
    else:
        print('NO')
