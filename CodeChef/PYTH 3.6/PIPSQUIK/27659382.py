for _ in range(int(input())):
    n, h, y1, y2, l = map(int, input().split())
    c = 0
    f = False

    for __ in range(n):
        t, x = map(int, input().split())

        if not f:
            if t == 1:
                if h - y1 <= x:
                    c += 1

                else:
                    if l != 1:
                        c += 1
                        l -= 1
                    else:
                        f = True

            if t == 2:
                if y2 >= x:
                    c += 1

                else:
                    if l != 1:
                        c += 1
                        l -= 1
                    else:
                        f = True

    print(c)
