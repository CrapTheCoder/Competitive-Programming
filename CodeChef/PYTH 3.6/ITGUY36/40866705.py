for _ in range(int(input())):
    n = int(input())
    l = [[' '] * n for _ in range(n)]

    for i in range(n):
        l[i][i] = '*'
        l[i][n-i-1] = '*'

    for i in l:
        print(*i, sep='')