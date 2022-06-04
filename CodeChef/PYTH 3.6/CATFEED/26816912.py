for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    x = list(range(1, n+1))

    for i in range(0, m - (m % n), n):
        if sorted(a[i:i+n]) != x:
            break
    else:
        if len(set(a[m-(m%n):m])) == len(a[m-(m%n):m]):
            print('YES')
        else:
            print('NO')

        continue

    print('NO')