for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    m = s = sum(a[:k])
    for i in range(k, n):
        s -= a[i-k]
        s += a[i]

        m = max(m, s)

    print(m)
