for _ in range(int(input())):
    n = int(input())

    s = list(range(1, 2*n+1))

    for i in range(n-1):
        print(' ' * i, end='')
        print(*s[i:2*n-i-1], sep='')

    for i in range(n-1, -1, -1):
        print(' ' * i, end='')
        print(*s[i:2*n-i-1], sep='')
