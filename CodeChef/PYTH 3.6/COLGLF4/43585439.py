for _ in range(int(input())):
    n, e, h, a, b, c = map(int, input().split())

    mini = float('inf')
    for z in range(min(n, e, h) + 1):
        nn = n - z
        ne = e - z
        nh = h - z
        cc = z * c

        if ne // 2 >= nn:
            ca = a * nn
            # print(1, ca, cc, ca + cc)
            mini = min(mini, ca + cc)
        else:
            nn -= ne // 2

            if nh // 3 >= nn:
                ca = a * (ne // 2)
                cb = b * nn
                # print(2, ca, cb, cc, ca + cb + cc)
                mini = min(mini, ca + cb + cc)

        nn = n - z
        ne = e - z
        nh = h - z
        cc = z * c

        if nh // 3 >= nn:
            cb = b * nn
            # print(3, cb, cc, cb + cc)
            mini = min(mini, cb + cc)
        else:
            nn -= nh // 3

            if ne // 2 >= nn:
                cb = b * (nh // 3)
                ca = a * nn
                # print(4, ca, cb, cc, ca + cb + cc)
                mini = min(mini, ca + cb + cc)

    if mini == float('inf'):
        print(-1)
    else:
        print(mini)
 