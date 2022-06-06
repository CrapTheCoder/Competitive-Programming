for _ in range(int(input())):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
 
    while x1 < x2 and p1 > 0:
        x1 *= 10
        p1 -= 1
 
    while x2 < x1 and p2 > 0:
        x2 *= 10
        p2 -= 1
 
    if len(str(x1)) > len(str(x2)) and str(x1)[-1] == '0':
        x1 //= 10
        p1 += 1
 
    if len(str(x2)) > len(str(x1)) and str(x2)[-1] == '0':
        x2 //= 10
        p2 += 1
 
    if p1 > p2:
        print('>')
    elif p1 < p2:
        print('<')
    else:
        if x1 > x2:
            print('>')
        elif x1 < x2:
            print('<')
        else:
            print('=')