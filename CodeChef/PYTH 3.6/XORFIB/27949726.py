for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(m, 2 * m):
        x = 0

        for j in range(i - m, i):
            x ^= a[j]

        a.append(x)

    a = a[m-1:]

    print(a[(n - m + 1) % (m + 1)])
