for _ in range(int(input())):
    q, p = map(int, input().split())
    c = p * q

    if q > 1000:
        c -= c * 0.1

    print('%.6f' % c)