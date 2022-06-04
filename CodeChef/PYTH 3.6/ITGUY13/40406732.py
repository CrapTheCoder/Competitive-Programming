for i in range(int(input())):
    x, n = map(int, input().split())
    a = list(map(int, input().split()))

    if x not in a:
        print(-1)
        continue

    d = a.index(x) + 1
    e = -1
    for i in range(n-1, -1, -1):
        if a[i] == x:
            e = i+1
            break

    if d == e:
        print(-1)
        continue

    print(d, e)