for _ in range(int(input())):
    n, k = map(int, input().split())

    if (n // (k * k)) * (k * k) == n:
        print('NO')
    else:
        print('YES')