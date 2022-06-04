for _ in range(int(input())):
    n, m = map(int, input().split())
    print(((n * (n - 1) // 2) - (m * (m - 1) // 2) + 1) % (10 ** 9 + 7))