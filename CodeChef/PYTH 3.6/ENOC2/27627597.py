for _ in range(int(input())):
    a, b = map(int, input().split())

    while a <= b:
        if not (b - a) % 2:
            break

        a *= 2
    else:
        print('NO')
        continue

    print('YES')