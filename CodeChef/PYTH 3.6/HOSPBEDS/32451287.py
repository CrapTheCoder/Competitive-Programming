def f(i, j):
    return 0 <= i < n and 0 <= j < n

for _ in range(int(input())):
    n = int(input())

    a = [list(map(int, input().split())) for _ in range(n)]

    vc = 0

    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                if f(i-1, j) and a[i-1][j] == 1: vc = 1
                if f(i+1, j) and a[i+1][j] == 1: vc = 1
                if f(i, j-1) and a[i][j-1] == 1: vc = 1
                if f(i, j+1) and a[i][j+1] == 1: vc = 1

    if vc == 1:
        print('UNSAFE')
    else:
        print('SAFE')
