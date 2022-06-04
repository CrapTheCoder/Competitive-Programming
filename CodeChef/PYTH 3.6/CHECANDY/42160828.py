def solve(a):
    s = 0
    for i in range(n):
        s += a[i]

    if s % 2 != 0:
        return False

    part = [[True for _ in range(n + 1)] for _ in range(s // 2 + 1)]

    for i in range(0, n + 1):
        part[0][i] = True

    for i in range(1, s // 2 + 1):
        part[i][0] = False

    for i in range(1, s // 2 + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            if i >= a[j - 1]:
                part[i][j] = (part[i][j] or part[i - a[j - 1]][j - 1])

    return part[s // 2][n]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if solve(a):
        print('Impressed')
    else:
        print('Not Impressed')
