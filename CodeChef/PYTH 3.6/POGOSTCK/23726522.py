for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    tm = float('-inf')

    for r in range(k):
        x = a[r::k]
        l = len(x)

        s = sum(x)
        m = s

        for i in range(l-1):
            s -= x[i]
            m = max(m, s)

        tm = max(tm, m)

    print(tm)
