for _ in range(int(input())):
    n, m, k = map(int, input().split())
    x = abs(n - m)

    print(max(x - k, 0))