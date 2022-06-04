for i in range(int(input())):
    n = int(input())

    l = [' '] * (n+1)
    l[-1] = n

    print(*l, sep='')

    for i in range(n-1, -1, -1):
        l[i] = i
        print(*l, sep='')

    for i in range(n + 1):
        l[i] = ' '
        print(*l, sep='')
