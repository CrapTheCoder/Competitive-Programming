for _ in range(int(input())):
    n = int(input())

    x = y = 0

    while x <= n:
        x += y + 1
        y += 1

    print(y - 1)