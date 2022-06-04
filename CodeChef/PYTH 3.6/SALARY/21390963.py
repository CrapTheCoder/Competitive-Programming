for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    c = 0

    while True:
        add = a[-1] - a[0]

        if add == 0:
            break

        for i in range(n - 1):
            a[i] += add

        a = sorted(a)
        c += add

    print(c)