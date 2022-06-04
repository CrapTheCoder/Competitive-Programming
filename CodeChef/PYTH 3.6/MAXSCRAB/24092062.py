for _ in range(int(input())):
    n = int(input())
    s = input()
    v = list(map(int, input().split()))

    ma = -1

    for x in range(n - 8 + 1):
        m = 1
        l = s[x:x+8]
        r = v.copy()

        for i in range(8):
            if l[i] == 'd': r[i] *= 2
            if l[i] == 't': r[i] *= 3

            if l[i] == 'D': m *= 2
            if l[i] == 'T': m *= 3

        ma = max(ma, sum(r) * m)

    print(ma)