try:
    p = int(input())

    a, b = 0, 1

    if p == a or p == b:
        print(p)
        exit()

    while True:
        if a < p < b:
            if (p - a) < (b - p):
                print(a)
            else:
                print(b)
            break

        a, b = b, a + b
except:
    pass