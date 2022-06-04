for _ in range(int(input())):
    n, a, b = map(int, input().split())
    l = list(map(int, input().split()))
    i = x = y = 0

    for i in range(n):
        x += l[i] == a
        y += l[i] == b

    print('%.8f' % (x / n * y / n))
