for _ in range(int(input())):
    n, b, m = map(int, input().split())
    s = 0

    while 0 < n:
        if n == 1:
            s += m
            break
        else:
            s += ((n + 1) // 2) * m + b
            m *= 2
            n //= 2

    print(s)