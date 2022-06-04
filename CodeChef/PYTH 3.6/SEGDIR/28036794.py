for _ in range(int(input())):
    n = int(input())

    d = {}

    for _ in range(n):
        l, r, v = map(int, input().split())

        d[v] = d.get(v, []) + [(l, r)]

    for l in list(d.values()):
        l.sort()

        x = len(l)

        f = 0

        for i in range(x):
            for j in range(i + 1, x):
                if l[j][0] <= l[i][1]:
                    for k in range(j + 1, x):
                        if l[k][0] <= l[i][1] and l[k][0] <= l[j][1]:
                            print('NO')
                            f = 1
                            break

                    if f:
                        break
            if f:
                break
        if f:
            break
    else:
        print('YES')
