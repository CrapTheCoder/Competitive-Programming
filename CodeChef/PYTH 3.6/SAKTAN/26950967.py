for _ in range(int(input())):
    n, m, q = map(int, input().split())

    ra = [0] * n
    ca = [0] * m

    for __ in range(q):
        r, c = map(int, input().split())

        ra[r-1] += 1
        ca[c-1] += 1

    re = ro = ce = co = 0

    for i in ra:
        if not i % 2:
            re += 1
        else:
            ro += 1

    for i in ca:
        if not i % 2:
            ce += 1
        else:
            co += 1

    print(re * co + ce * ro)
