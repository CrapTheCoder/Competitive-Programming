for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    l = [a[0], a[1]]

    for i in range(2, n-1):
        l.append(l[-2] + a[i])

    l = [0] + l

    for __ in range(q):
        p, q = sorted(map(int, input().split()))
        p -= 1
        q -= 1

        if not (p - q) % 2:
            print('UNKNOWN')
        else:
            print(l[q] - l[q-1] + l[p] - (l[p-1] if p-1 >= 0 else 0))
