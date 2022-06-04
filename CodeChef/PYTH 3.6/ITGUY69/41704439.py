for _ in range(int(input())):
    n = int(input()) - 2
    s = list(range(1, n+1))

    l = n // 2

    c = 1
    for i in range(n-l, 0, -1):
        print(' ' * i, str(c) * l)
        c += 1

    for i in range(n-l+1):
        print(' ' * i, str(c) * l)
        c += 1