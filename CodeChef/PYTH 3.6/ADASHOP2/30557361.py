for _ in range(int(input())):
    r, c = map(int, input().split())

    if not (r == c == 1):
        print(27)
        print((r + c) // 2, (r + c) // 2)
        print(1, 1)
    else:
        print(25)

    for i in range(2, 8):
        print(i, i)

        if i <= 4:
            print(1, 2 * i - 1)
            print(2 * i - 1, 1)
        else:
            print(8, 2 * (i - 4))
            print(2 * (i - 4), 8)

        print(i, i)

    print(8, 8)
