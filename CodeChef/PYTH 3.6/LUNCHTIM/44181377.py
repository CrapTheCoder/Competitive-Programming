for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for j, i in enumerate(a):
        d[i] = d.get(i, []) + [j]

    s = []
    b = [0] * n

    for i in range(n-1, -1, -1):
        while len(s) > 0 and s[-1][0] <= a[i]:
            s.pop()

        if len(s) == 0:
            b[i] = (float('inf'), float('inf'))
        else:
            b[i] = s[-1]

        s.append((a[i], i))

    vis = set()
    c = [0] * n

    for i, (j, k) in enumerate(b):
        if i in vis:
            continue

        t = d[a[i]].index(i)
        f = 0

        for l in range(t+1, len(d[a[i]])):
            if d[a[i]][l] >= k:
                break

            f += 1

        for l in range(t, len(d[a[i]])):
            if d[a[i]][l] >= k:
                break

            c[d[a[i]][l]] += f
            vis.add(d[a[i]][l])

    print(*c)