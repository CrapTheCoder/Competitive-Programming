for _ in range(int(input())):
    n, q = map(int, input().split())
    s = list(map(int, input().split()))

    x = []

    for __ in range(q):
        x.append(int(input()))

    d = {}

    for i in s:
        d[i] = d.get(i, 0) + 1

    l = [0]

    for i in sorted(d.values(), reverse=True):
        l.append(i + l[-1])

    for k in x:
        print(l[min(k, len(l) - 1)])
