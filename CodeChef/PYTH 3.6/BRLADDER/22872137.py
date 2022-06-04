for _ in range(int(input())):
    n, m = map(int, input().split())

    if n > m: n, m = m, n

    if n % 2:
        print('YES' if m in [n-2, n+1, n+2] else 'NO')
    else:
        print('YES' if m in [n-1, n-2, n+2] else 'NO')