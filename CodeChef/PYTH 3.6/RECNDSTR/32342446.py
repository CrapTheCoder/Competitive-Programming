for _ in range(int(input())):
    s = input()

    l = s[1:] + s[0]
    r = s[-1] + s[:-1]

    if l == r:
        print('YES')
    else:
        print('NO')