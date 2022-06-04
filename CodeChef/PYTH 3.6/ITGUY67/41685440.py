for _ in range(int(input())):
    n = int(input())
    l = [[0] * n for _ in range(n)]

    i = n // 2
    j = (n-1) // 2

    if n % 2 == 1:
        x, y = 0, -1
    else:
        x, y = 0, 1
    l[i][j] = 1

    c = 1

    g = 0
    while (i, j) != (0, 0):
        for _ in range(g // 2 + 1):
            if not ((0 <= i+x < n) and (0 <= j+y < n)):
                break

            c += 1
            i += x
            j += y

            l[i][j] = c

        if y == -1: x, y = 1, 0
        elif x == 1: x, y = 0, 1
        elif y == 1: x, y = -1, 0
        elif x == -1: x, y = 0, -1

        g += 1

    for i in l:
        print(*i)