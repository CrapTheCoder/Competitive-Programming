for _ in range(int(input())):
    c, d, l = list(map(int, input().split()))

    x = -1

    if c <= 2 * d:
        x = d * 4
    else:
        x = (c - d) * 4

    y = (c + d) * 4

    if l % 4 == 0 and x <= l <= y:
        print('yes')
    else:
        print('no')