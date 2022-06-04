for _ in range(int(input())):
    n, q = map(int, input().split())

    a = [[] for _ in range(n+1)]
    b = [[] for _ in range(n+1)]

    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1

        a[l].append(1)
        b[r].append(r - l)

    tot = cnt = 0

    for i in range(n):
        for j in a[i]:
            cnt += 1

        for j in b[i]:
            tot -= j
            cnt -= 1

        tot += cnt

        print(tot, end=' ')

    print()
