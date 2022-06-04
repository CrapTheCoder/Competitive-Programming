for _ in range(int(input())):
    a, b, x = map(int, input().split())

    print((b - a) // x + 1)