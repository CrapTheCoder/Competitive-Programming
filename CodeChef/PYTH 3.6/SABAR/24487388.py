for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a + b - 1, max(a, b) - min(a, b) + 1)
