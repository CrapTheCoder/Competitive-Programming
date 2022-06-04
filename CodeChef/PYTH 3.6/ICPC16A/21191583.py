for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    d1 = x1 == x2
    d2 = y1 == y2

    if d1 == d2:
        print('sad')
    else:
        if d1:
            if y1 < y2:
                print('up')
            else:
                print('down')
        if d2:
            if x1 < x2:
                print('right')
            else:
                print('left')