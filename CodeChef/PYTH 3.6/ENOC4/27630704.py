for _ in range(int(input())):
    n, k = map(int, input().split())
    x = n // k

    print((((x * (x + 1)) // 2) * (k * 2) + n) % (10 ** 9 + 7))