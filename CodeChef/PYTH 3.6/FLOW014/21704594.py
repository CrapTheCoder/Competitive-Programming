for _ in range(int(input())):
    h, c, t = map(float, input().split())

    x = h > 50
    y = c < 0.7
    z = t > 5600

    if x and y and z:
        print('10')
    elif x and y:
        print('9')
    elif y and z:
        print('8')
    elif x and z:
        print('7')
    elif [x, y, z].count(True) == 1:
        print('6')
    else:
        print('5')