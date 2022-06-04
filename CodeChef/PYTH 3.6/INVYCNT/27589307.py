last = 0

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    l1 = []
    l2 = []

    for i in range(n):
        c = 0

        for j in range(i + 1, n):
            c += a[i] > a[j]

        l1.append(c)

    for i in range(n):
        c = 0

        for j in range(n):
            c += a[i] > a[j]

        l2.append(c)

    s = 0

    for i in range(n):
        x = l1[i]
        y = l2[i]

        z = ((k - 1) * k // 2) * y + x * k

        s += z

    print(s)
