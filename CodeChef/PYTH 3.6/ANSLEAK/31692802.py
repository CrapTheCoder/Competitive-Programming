for _ in range(int(input())):
    n, m, k = map(int, input().split())

    d = []

    for i in range(n-1, -1, -1):
        a = list(map(int, input().split()))

        d.append(a[i])

    print(*d)
