for _ in range(int(input())):
    n = int(input()) - 2
    s = list(range(1, n+1))

    l = n // 2

    for i in range(n-l, 0, -1):
        print(' ' * i, *s[i:i+l], sep='')

    for i in range(n-l+1):
        print(' ' * i, *s[i:i+l], sep='')