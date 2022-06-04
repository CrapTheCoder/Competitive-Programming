for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split())) + [-1]

    c = []
    cl = 0
    s = ''

    for i in range(n):
        if i == 0:
            c.append(str(a[i]))
            cl += 1
            continue

        if a[i] == a[i - 1] + 1:
            c.append(str(a[i]))
            cl += 1
        else:
            if cl > 2:
                s += c[0] + '...' + c[-1] + ','
            else:
                for j in c:
                    s += j + ','

            c = [str(a[i])]
            cl = 1

    if len(c) > 2:
        s += c[0] + '...' + c[-1]
    else:
        s += ','.join(c)

    print(s)
