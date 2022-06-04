for _ in range(int(input())):
    b, g = map(int, input().split())

    b, g = sorted((b, g))

    print(2 * g + (b - 1) * 2)