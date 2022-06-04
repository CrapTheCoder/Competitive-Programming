for _ in range(int(input())):
    n = int(input()) - 2
    s = list(range(1, n+1))

    l = n // 2

    c = 1
    for i in range(n-l, 0, -1):
        print(' ' * i, end='')
        for _ in range(l):
            print(c, end='')
            c += 1

        print()

    for i in range(n-l+1):
        print(' ' * i, end='')
        for _ in range(l):
            print(c, end='')
            c += 1

        print()