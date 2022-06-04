for _ in range(int(input())):
    a = sorted(map(int, input()))

    for i in range(1, len(a)):
        if a[i] - a[i - 1] > 2:
            print('NO')
            break
    else:
        print('YES')