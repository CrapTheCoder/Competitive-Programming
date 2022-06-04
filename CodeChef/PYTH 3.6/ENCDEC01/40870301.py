for _ in range(int(input())):
    n, x = map(int, input().split())
    a = sorted(map(int, input().split()))

    if (a[-1] - a[0]) < x:
        print('YES')
    else:
        print('NO')
