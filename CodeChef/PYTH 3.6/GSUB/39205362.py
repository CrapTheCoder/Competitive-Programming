for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    c = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            c += 1

    for _ in range(q):
        x, y = map(int, input().split())
        x -= 1

        d1 = False
        if x > 0:
            d1 = a[x-1] == a[x]

        d2 = False
        if x < n-1:
            d2 = a[x+1] == a[x]

        if a[x] == y:
            print(c)
            continue

        a[x] = y

        if (x > 0) and (not d1) and (a[x-1] == a[x]): c -= 1
        if (x < n-1) and (not d2) and (a[x+1] == a[x]): c -= 1

        if (x > 0) and d1 and (a[x-1] != a[x]): c += 1
        if (x < n-1) and d2 and (a[x+1] != a[x]): c += 1

        print(c)
