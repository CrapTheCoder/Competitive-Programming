for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    m = 10000000000

    for i in range(n - 1):
        if m > a[i + 1] - a[i]:
            m = a[i + 1] - a[i]

    print(m)
