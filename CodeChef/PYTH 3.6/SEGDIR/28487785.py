for _ in range(int(input())):
    n = int(input())

    d = {}

    for _ in range(n):
        l, r, v = map(int, input().split())

        d[v] = d.get(v, []) + [(l, r)]

    f = False

    for a in d.values():
        a.sort()
        n = len(a)

        for i in range(n):
            for j in range(i+1, n):
                if a[j][0] <= a[i][1]:
                    for k in range(j+1, n):
                        if a[k][0] <= a[i][1] and a[k][0] <= a[j][1]:
                            f = True

    if f:
        print('NO')
    else:
        print('YES')

"""

1
3
2 4 1
3 6 1
5 8 1

"""