for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    x = sum(a[k:-k]) / (n - 2 * k)

    if k == 0:
        x = sum(a) / n

    print('%.6f' % x)