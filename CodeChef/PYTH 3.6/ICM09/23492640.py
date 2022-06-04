for _ in range(int(input())):
    n = int(input())
    s = input()

    c = c0 = c1 = 0

    for i in s:
        if i == '0': c0 += 1
        if i == '1': c1 += 1

        if c0 > c1:
            c += 1
            c1 += 1
            c0 -= 1

    print(c)