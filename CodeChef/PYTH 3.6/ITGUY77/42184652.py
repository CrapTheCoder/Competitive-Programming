for _ in range(int(input())):
    n = int(input())

    if n % 2 == 0:
        s = 'A'
    else:
        s = '*'

    for i in range(n-1, -1, -1):
        print(' ' * i + s + ' ' * i)
        if i % 2 == 0:
            s = 'A' + s + 'A'
        else:
            s = '*' + s + '*'