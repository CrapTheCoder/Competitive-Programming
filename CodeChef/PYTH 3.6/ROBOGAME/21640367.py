for _ in range(int(input())):
    d = []
    n = 0
    s = input()

    for i, j in enumerate(s, 1):
        if j != '.':
            l = i - int(j)
            r = i + int(j)

            d.append([l, r])

            n += 1

    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = d[i]
            x2, y2 = d[j]

            if x2 <= y1:
                print('unsafe')
                break
        else:
            continue
        break
    else:
        print('safe')