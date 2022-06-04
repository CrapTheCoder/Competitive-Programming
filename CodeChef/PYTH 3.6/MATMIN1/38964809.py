for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [input().split() for _ in range(n)]
    s = input()
    p, q = map(int, input().split())

    t = 0

    for i, j in enumerate(s):
        c = 0

        if i >= m:
            x = i-m+1
            y = m-1
        else:
            x = 0
            y = i

        f = 0

        while 0 <= x < n and 0 <= y < m:
            c += a[x][y] != j
            f += 1

            x += 1
            y -= 1

        t += min(c * p, p * (f-c) + q)

    print(t)
