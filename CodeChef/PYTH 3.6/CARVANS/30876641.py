for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = 1

    for i in range(1, n):
        copy = a[i]

        a[i] = min(a[i], a[i-1])

        if a[i] == copy:
            m += 1

    print(m)