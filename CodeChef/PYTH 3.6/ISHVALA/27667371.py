for _ in range(int(input())):
    n, m = map(int, input().split())
    xc, yc, s = map(int, input().split())

    x = []
    y = []

    if xc: x = list(map(int, input().split()))
    if yc: y = list(map(int, input().split()))

    x = [0] + x + [n + 1]
    y = [0] + y + [m + 1]

    l1 = 0
    l2 = 0

    for i in range(1, xc + 2): l1 += (x[i] - x[i-1] - 1) // s
    for i in range(1, yc + 2): l2 += (y[i] - y[i-1] - 1) // s

    print(l1 * l2)
