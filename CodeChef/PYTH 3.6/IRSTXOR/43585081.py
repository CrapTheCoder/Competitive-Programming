for _ in range(int(input())):
    c = int(input())
    x = bin(c)[2:]

    a = '1'
    b = '0'

    for i in x[1:]:
        if i == '0':
            a += '1'
        else:
            a += '0'

        b += '1'

    print(int(a, 2) * int(b, 2))
