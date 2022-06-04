for _ in range(int(input())):
    n, m, k = map(int, input().split())

    c = [0] * k
    r = []

    for _ in range(n):
        a = list(map(int, input().split()))

        d = {}

        for i, j in enumerate(a):
            d[j] = d.get(j, []) + [i]

        cc = c
        mini, maxi = min(c), max(c)

        choice = -1

        for i in d:
            nc = c.copy()

            for j in d[i]:
                nc[j] += 1

            cmini, cmaxi = min(nc), max(nc)

            if (mini, maxi) < (cmini, cmaxi):
                cc = nc
                mini, maxi = cmini, cmaxi

                choice = i

        r.append(choice)

        c = cc

    print(*r)
