for _ in range(int(input())):
    n = int(input())

    l = [[' '] * i for i in range(1, n+1)]

    for i in range(n-1):
        l[i][0] = l[i][-1] = '*'
        print(*l[i], sep='')

    print('*' * n)