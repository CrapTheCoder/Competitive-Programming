for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c = 1
    m = a[0]

    for i in range(1, n):
        if a[i] <= m:
            c += 1
            m = a[i]

    print(c)