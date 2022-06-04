for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    p = []
    m = float('inf')
    mi = -1

    for i in range(n):
        if m > a[i]:
            m = a[i]

        p.append(m)
        m += 1

    s = []
    m = float('inf')
    mi = -1

    for i in range(n-1, -1, -1):
        if m > a[i]:
            m = a[i]

        s.append(m)
        m += 1

    s.reverse()

    print(*(min(p[i], s[i]) for i in range(n)))