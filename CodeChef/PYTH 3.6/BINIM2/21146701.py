for _ in range(int(input())):
    n, s = input().split()
    n = int(n)

    c1 = 0
    c2 = 0

    for i in range(n):
        b = input()

        if b[0] == b[-1] == '0':
            c1 += 1
        elif b[0] == b[-1] == '1':
            c2 += 1
        else:
            c1 += 1
            c2 += 1

    if c2 > c1:
        print('Dee')
    elif c2 < c1:
        print('Dum')
    else:
        print(s)
