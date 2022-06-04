for _ in range(int(input())):
    n, m = map(int, input().split())
    f = False
    lis = []

    for __ in range(n):
        want, result = input().split()

        if want == 'correct':
            if '0' in result:
                f = True
        else:
            if '0' not in result:
                lis.append('x')
    else:
        if f:
            print('INVALID')
        elif lis:
            print('WEAK')
        else:
            print('FINE')