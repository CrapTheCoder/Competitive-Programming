for _ in range(int(input())):
    n = int(input())
    a = input()

    if ('cookie cookie' in a) or a[-6:] == 'cookie':
        print('NO')
    else:
        print('YES')