for _ in range(int(input())):
    n, m = map(int, input().split())

    a = list(range(1, n+1))
    b = list(map(int, input().split()))

    for i in b:
        a.remove(i)

    print(*a[0::2])
    print(*a[1::2])