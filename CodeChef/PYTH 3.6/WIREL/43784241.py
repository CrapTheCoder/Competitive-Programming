n, m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())

for _ in range(m):
    a, b, c, d = map(int, input().split())
    e, f, g, h = 10 ** 6 - a, 10 ** 6 - b, 10 ** 6 - c, 10 ** 6 - d

    print(*min(
        ((a+1) ** 2 + b ** 2, (-(a+1), -b)),
        (a ** 2 + (b+1) ** 2, (-a, -(b+1))),
        ((c+1) ** 2 + d ** 2, (-(c+1), -d)),
        (c ** 2 + (d+1) ** 2, (-c, -(d+1))),
        ((e+1) ** 2 + f ** 2, (e+1, f)),
        (e ** 2 + (f+1) ** 2, (e, f+1)),
        ((g+1) ** 2 + d ** 2, (g+1, d)),
        (g ** 2 + (d+1) ** 2, (g, d+1)),
    )[-1])