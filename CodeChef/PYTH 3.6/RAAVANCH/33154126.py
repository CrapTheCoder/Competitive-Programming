for _ in range(int(input())):
    n, k, x = map(int, input().split())

    s = [0] * (k-1) + [x]

    print(*(s * (n // k) + s)[:n])
