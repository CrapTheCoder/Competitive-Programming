for _ in range(int(input())):
    n, k = map(int, input().split())
    print(k * (k + 1) // 2 + (n - k))