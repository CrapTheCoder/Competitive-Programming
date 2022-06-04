for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))

    d = {}

    for i in a:
        d[i] = 1

    c = 0

    a = list(d.keys())

    for i in a:
        if not i & 1:
            if i >> 1 not in d:
                d[i >> 1] = 1
                a.append(i >> 1)

            c += 1

    print(c)
