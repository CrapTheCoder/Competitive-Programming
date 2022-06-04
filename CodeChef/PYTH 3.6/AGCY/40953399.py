for _ in range(int(input())):
    n, q = map(int, input().split())

    a = [0] * n
    b = [0] * (n+1)
    c = [0] * (n+1)

    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1

        a[l] += 1
        b[r] += r-l
        c[r] += 1

    tot = cnt = 0

    for i in range(n):
        cnt += a[i] - c[i]
        tot += cnt - b[i]

        print(tot, end=' ')

    print()
