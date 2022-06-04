for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    d = {}

    pr = [a[0]]
    for i in range(1, n):
        pr.append(pr[-1] + a[i])

    su = [a[-1]]
    for i in range(n-2, -1, -1):
        su.append(su[-1] + a[i])
    su.reverse()

    for i in range(n):
        d[a[i]] = d.get(a[i], [-1, -1])
        if d[a[i]][0] == -1:
            d[a[i]][0] = i

        d[a[i]][1] = i

    for _ in range(q):
        x = int(input())

        print(min(pr[d[x][0]], su[d[x][1]]))
