for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    d = {}
    x = 0

    f = [0] * n

    for i in range(n):
        if a[i] in d:
            if d[a[i]] == 1:
                x += 2
            else:
                x += 1

        d[a[i]] = d.get(a[i], 0) + 1

        e = {}
        y = 0

        f[i] = x + k

        asd = []

        for j in range(i, -1, -1):
            f[i] = min(f[j] + k + y, f[i])

            if a[j] in e:
                if e[a[j]] == 1:
                    y += 2
                else:
                    y += 1

            asd.append(y)

            e[a[j]] = e.get(a[j], 0) + 1

    print(f[-1])
