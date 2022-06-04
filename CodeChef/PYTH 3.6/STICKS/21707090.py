for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dum = []
    dic = {0: 1}

    for i in a:
        dic[i] = dic.get(i, 0) + 1
    for i in dic:
        dum.append((i, dic[i]))

    dum = sorted(dum, reverse=True)

    x = []

    for i, j in dum:
        if j > 1:
            x.append(i)
        if j > 3:
            x.append(i)

        if len(x) >= 2:
            break

    if len(x) >= 2:
        print(x[0] * x[1])
    else:
        print(-1)
