def isValid(x, y, f, o):
    if x >= f and y >= o:
        return 1
    return 0

for _ in range(int(input())):
    n = int(input())
    f = o = 0

    for __ in range(n):
        x, a, b = map(int, input().split())

        if x == 1:
            f, o = a, b
            print('YES')

        if x == 2:
            if a == b:
                f, o = a, b
                print('YES')
            else:
                r = isValid(a, b, f, o)
                s = isValid(b, a, f, o)

                if r and s:
                    print('NO')
                elif r:
                    f, o = a, b
                    print('YES')
                elif s:
                    f, o = b, a
                    print('YES')