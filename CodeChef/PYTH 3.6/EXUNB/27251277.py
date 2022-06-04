for _ in range(int(input())):
    n = int(input())

    if not n % 2:
        print('NO')
    else:
        x = ['0'] * n
        x[: n // 2] = ['1'] * (n // 2)

        print('YES')

        for i in list(range(1, n)) + [0]:
            x = [x[-1]] + x[:-1]
            print(''.join(x))

