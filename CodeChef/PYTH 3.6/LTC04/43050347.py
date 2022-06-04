for _ in range(int(input())):
    t, a, b = input().split()
    a = a.lower()
    b = b.lower()

    if t == 'A':
        print(a + b.capitalize())
    elif t == 'B':
        print(a + '_' + b)
    elif t == 'C':
        print((a + '_' + b).upper())
    elif t == 'D':
        print(a.capitalize() + '-' + b.capitalize())

    else:
        ns = ''
        for i, j in enumerate(a):
            if i % 2:
                ns += j.upper()
            else:
                ns += j

        ns += '|'

        for i, j in enumerate(b):
            if i % 2:
                ns += j.upper()
            else:
                ns += j

        print(ns)