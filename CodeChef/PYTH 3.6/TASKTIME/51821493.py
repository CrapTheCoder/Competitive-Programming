for _ in range(int(input())):
    n, m, k = map(int, input().split())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))

    l = [[] for _ in range(m)]

    for i in range(n):
        l[c[i]-1].append(t[i])

    new = []

    for i in range(m):
        if not l[i]:
            continue

        l[i].sort()

        nl = [l[i][0]]

        try:
            for j in range(1, len(l[i]), 2):
                nl.append(l[i][j] + l[i][j+1])
        except:
            pass

        new += nl

    new.sort()

    c = 0
    for i in new:
        if k - i >= 0:
            k -= i
        else:
            break
        
        c += 1

    print(c)
