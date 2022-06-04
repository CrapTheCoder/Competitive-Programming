for _ in range(int(input())):
    n = int(input())
    ls = []
    rs = []
    lrs = []

    for i in range(n):
        l, r = map(int, input().split())
        ls.append(l)
        rs.append(r)
        lrs.append((l, r, i))

    lrs.sort()

    c = 0
    maxi = -1

    res = [-1] * n
    for l, r, i in lrs:
        if ls[i] > maxi:
            maxi = rs[i]
            res[i] = c

        elif rs[i] <= maxi:
            res[i] = 1^c

        else:
            maxi = rs[i]
            c ^= 1
            res[i] = c

    print(*res, sep='')