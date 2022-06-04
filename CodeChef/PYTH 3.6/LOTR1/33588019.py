for _ in range(int(input())):
    n, m = map(int, input().split())
    y = '9'

    c = 0

    while True:
        if int(y) > m:
            break

        if 1 <= int(y) <= m:
            c += 1

        y += '9'

    print(c * n, n)