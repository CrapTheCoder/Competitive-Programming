for _ in range(int(input())):
    s = input()
    d = {}

    for i in range(len(s)):
        x = d.get(s[i], [i, -1])
        x[1] = i

        d[s[i]] = x

    mc = ''
    m = -1

    for i, j in zip(d.keys(), d.values()):
        if j[1] - j[0] > m:
            m = j[1] - j[0]
            mc = i

        elif j[1] - j[0] == m and i < mc:
            mc = i

    print(mc, m)