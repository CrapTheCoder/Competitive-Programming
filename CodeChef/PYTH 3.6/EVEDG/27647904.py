for _ in range(int(input())):
    n, m = map(int, input().split())

    g = [[] for __ in range(n)]
    l = [0] * n

    r = [1] * n

    for __ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        g[u].append(v)
        g[v].append(u)

        l[u] += 1
        l[v] += 1

    d = 1

    if not m % 2:
        print(1)
        print(*r)
    else:
        for i in range(n):
            if l[i] % 2 and l[i] != 0:
                d = 2
                r[i] = 2
                break
        else:
            for i in range(n):
                if l[i]:
                    d = 3
                    r[i] = 2
                    r[g[i][0]] = 3

                    break

        print(d)
        print(*r)