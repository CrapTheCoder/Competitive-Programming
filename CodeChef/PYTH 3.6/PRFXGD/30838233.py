for _ in range(int(input())):
    s = input()
    k, x = map(int, input().split())

    c = {}

    good = 0

    for i in s:
        c[i] = c.get(i, 0) + 1

        if c[i] > x:
            if k != 0:
                c[i] -= 1
                k -= 1
            else:
                break
        else:
            good += 1

    print(good)
