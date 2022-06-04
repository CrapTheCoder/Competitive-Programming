for _ in range(int(input())):
    a, b, c = [], [0, 0, 0, 0], [0, 0, 0, 0]

    for j in range(12):
        l = input().split()

        if l[0] not in a or l[4] not in a:
            if l[0] not in a: a.append(l[0])
            if l[4] not in a: a.append(l[4])

        i1, i2 = a.index(l[0]), a.index(l[4])

        if int(l[1]) > int(l[3]):
            b[i1] = b[i1] + 3
            c[i1] += int(l[1]) - int(l[3])
            c[i2] += int(l[3]) - int(l[1])

        if int(l[1]) < int(l[3]):
            b[i2] = b[i2] + 3
            c[i1] += int(l[1]) - int(l[3])
            c[i2] += int(l[3]) - int(l[1])

        if int(l[1]) == int(l[3]):
            b[i2], b[i1] = b[i2] + 1, b[i1] + 1

    x = [[a[i], b[i], c[i]] for i in range(4)]
    x = sorted(x, key=lambda x: x[1] * 100 + x[2])
    print(f'{x[3][0]} {x[2][0]}')
