from bisect import insort

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    d = {}

    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1

    b = sorted(d.values())

    for i in range(min(k, n)):
        x = b.pop()

        if x == 1:
            break

        insort(b, x - 1)

    print((n * (n - 1) // 2) - sum(i * (i - 1) // 2 for i in b))