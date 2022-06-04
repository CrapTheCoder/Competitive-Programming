for _ in range(int(input())):
    s, sg, fg, d, t = map(int, input().split())

    v = s + (d * 50) * 3.6 / t

    a = abs(sg - v)
    b = abs(fg - v)

    if b > a:
        print('SEBI')
    elif a > b:
        print('FATHER')
    else:
        print('DRAW')