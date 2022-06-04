for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if any(i >= x for i in a):
        print('YES')
    else:
        print('NO')