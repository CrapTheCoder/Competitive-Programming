for _ in range(int(input())):
    n, k, p = map(int, input().split())
    a = list(map(int, input().split()))

    if k % 2 == 1:
        if p == 0: print(max(a))
        if p == 1: print(min(a))

    if k % 2 == 0:
        if p == 0:
            a.append(float('inf'))
            m = -1

            for i in range(n):
                m = max(m, min(a[i-1], a[i+1]))

            print(m)

        if p == 1:
            a.append(-1)
            m = float('inf')

            for i in range(n):
                m = min(m, max(a[i - 1], a[i + 1]))

            print(m)
