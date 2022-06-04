for _ in range(int(input())):
    n = int(input())
    l = [list(map(int, input().split())) for i in range(n)]

    m = 0

    for i in range(n):
        s, x, y = 0, i, 0

        while x < n and y < n:
            s += l[x][y]
            x += 1
            y += 1

        m = max(m, s)

    for i in range(n):
        s, x, y = 0, 0, i

        while x < n and y < n:
            s += l[x][y]
            x += 1
            y += 1

        m = max(m, s)

    print(m)

