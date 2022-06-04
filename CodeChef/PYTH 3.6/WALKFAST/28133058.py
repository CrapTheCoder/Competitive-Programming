for _ in range(int(input())):
    n, a, b, c, d, p, q, y = map(int, input().split())

    a -= 1
    b -= 1
    c -= 1
    d -= 1

    x = list(map(int, input().split()))

    m = p * abs(x[a] - x[b])

    if abs(x[a] - x[c]) * p <= y:
        m = min(m, y + (abs(x[c] - x[d]) * q) + (abs(x[d] - x[b]) * p))

    print(m)
