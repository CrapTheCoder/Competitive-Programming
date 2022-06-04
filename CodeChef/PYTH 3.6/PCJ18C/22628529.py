for i in range(int(input())):
    n, a, k = map(int, input().split())
    dn = n * (n - 1)
    nm = a * dn + 2 * (k - 1) * (180 * (n - 2) - a * n)

    x, y = dn, nm % dn

    while y > 0:
        x, y = y, x % y

    print(nm // x, dn // x)
