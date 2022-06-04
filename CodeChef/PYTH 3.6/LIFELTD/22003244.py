for _ in range(int(input())):
    a = input()
    b = input()
    c = input()

    x = False

    if a[0] == b[0] == b[1] == 'l': print('yes')
    elif a[1] == b[1] == b[2] == 'l': print('yes')
    elif b[0] == c[0] == c[1] == 'l': print('yes')
    elif b[1] == c[1] == c[2] == 'l': print('yes')
    else: print('no')