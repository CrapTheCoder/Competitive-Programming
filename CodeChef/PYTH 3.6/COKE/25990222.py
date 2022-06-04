for _ in range(int(input())):
    n, m, k, l, r = map(int, input().split())
    x = float('inf')

    for q in range(n):
        c, p = map(int, input().split())

        if m >= abs(c - k):
            c = k
        else:
            if k < c: c -= m
            if k > c: c += m

        if l <= c <= r and x > p:
            x = p

    if x == float('inf'):
        print(-1)
    else:
        print(x)