for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    bc = [0] * 32
    for i in a:
        for j in range(32):
            if i >> j & 1:
                bc[j] += 1

    t = 0
    for i, j in enumerate(bc):
        if j == n:
            t |= 1 << i

    c = 0
    p = a[0]

    for i in range(1, n):
        if p == t:
            p = a[i]

        else:
            p &= a[i]
            c += 1

    if p != t:
        c += 1

    print(c)