def fun(i=0, j=0):
    if x[i][j] == 1:
        return False

    if l[i][j] % 2:
        return False

    if i == j == n-1:
        print('YES')
        return True

    x[i][j] = 1

    m = 0

    try:
        if not l[i + 1][j] % 2:
            if fun(i + 1, j):
                return True
            else:
                m += 1
    except:
        m += 1

    try:
        if not l[i][j + 1] % 2:
            if fun(i, j + 1):
                return True
            else:
                m += 1
    except:
        m += 1

    if m == 2:
        return False

n = int(input().strip())

l = [list(map(int, input().strip().split())) for i in range(n)]
x = [[0] * n for _ in range(n)]

if not fun():
    print('NO')