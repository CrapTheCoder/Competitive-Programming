for _ in range(int(input())):
    s = list(input())
    sa, sb = map(int, input().split())

    x, y = s.index('A'), s.index('B')

    while x <= y:
        if x == y:
            print('unsafe')
            break

        x += sa
        y -= sb

    else:
        print('safe')
