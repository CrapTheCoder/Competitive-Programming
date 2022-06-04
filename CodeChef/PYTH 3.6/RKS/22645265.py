for _ in range(int(input())):
    n, k = map(int, input().split())

    r = set(range(1, n+1))
    c = r.copy()

    for l in range(k):
        x, y = map(int, input().split())

        r.remove(x)
        c.remove(y)

    print(n-k, end=' ')

    r = list(r)
    c = list(c)

    for i in range(n-k):
        print(r[i], c[i], end=' ')

    print()