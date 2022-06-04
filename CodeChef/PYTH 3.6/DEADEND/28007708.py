for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    c = 0
    i = 0

    while i < n:
        if i - 1 >= 0 and a[i - 1] == a[i] - 1:
            i += 1
            continue

        if i + 1 < n and a[i + 1] == a[i] + 1:
            i += 1
            continue

        a.insert(i+1, a[i] + 1)
        n += 1
        i += 2
        c += 1

    print(c)
