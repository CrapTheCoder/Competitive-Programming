for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)

    if n == 1 or len(s) > 2:
        print(-1)
        continue

    if len(s) == 1:
        x = s.pop()

        if x == 0:
            print(n)
        elif x == n-1:
            print(0)
        else:
            print(-1)

        continue

    x, y = sorted(s)
    xc, yc = a.count(x), a.count(y)

    if xc == y:
        print(yc)
    else:
        print(-1)
