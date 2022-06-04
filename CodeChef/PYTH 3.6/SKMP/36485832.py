for _ in range(int(input())):
    s = input()
    p = input()

    d = {}

    for i in s:
        d[i] = d.get(i, 0) + 1

    for i in p:
        d[i] -= 1

    n = sorted(d[i] * i for i in d.keys())
    n = ''.join(n)

    x = n + p

    for i in range(len(n)):
        y = n[:i] + p + n[i:]
        x = min(x, y)

    print(x)
