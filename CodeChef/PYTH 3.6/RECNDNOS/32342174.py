for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}

    for i, j in enumerate(a):
        d[j] = d.get(j, []) + [i]

    maxi = 0
    maxiv = 0

    for k, v in d.items():
        x = [v[0]]

        for i in range(1, len(v)):
            if x[-1] + 1 != v[i]:
                x.append(v[i])

        if len(x) > maxi:
            maxi = len(x)
            maxiv = k

        elif len(x) == maxi and k < maxiv:
            maxiv = k

    print(maxiv)