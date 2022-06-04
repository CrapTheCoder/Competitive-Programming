for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if a + 2*c >= b:
        print('YES')
    else:
        print('NO')