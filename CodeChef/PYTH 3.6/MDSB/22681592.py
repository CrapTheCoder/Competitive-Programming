for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = 0
    l = -1
    x = y = 0

    while y < n:
        while y < n and a[y]: y += 1
        if m < y - x and l != -1: m = y - x

        x = l + 1
        l = y
        y += 1

    if m < y - x and l != -1: m = y - x

    print(m)