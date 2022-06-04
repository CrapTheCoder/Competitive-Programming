for _ in range(int(input())):
    x, y = map(int, input().split())

    print((x * 2), (x*y) * (x*y-1))