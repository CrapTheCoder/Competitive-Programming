for _ in range(int(input())):
    x, y, k = map(int, input().split())

    if x % k == y % k == 0:
        print('YES')
    else:
        print('NO')