for _ in range(int(input())):
    n, m, b = map(int, input().split())

    c0 = c1 = 0

    for _ in range(n):
        x0, y0 = map(int, input().split())

        if y0 > m * x0 + b: c0 += 1
        if y0 < m * x0 + b: c1 += 1

    print(c0 * c1)