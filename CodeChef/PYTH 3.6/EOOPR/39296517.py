for _ in range(int(input())):
    x, y = map(int, input().split())

    if x == y:
        print(0)
        continue

    if x < y:
        d = y - x
        while d % 2 == 0:
            d //= 2

        print(min((y - x) // d, 3))

    if x > y:
        if (x - y) % 2 == 0:
            print(1)
        else:
            print(2)
