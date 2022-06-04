for _ in range(int(input())):
    n = int(input())
    s = []

    for __ in range(n):
        s += list(input())

    c = 0
    m = 'codechef'

    f = False

    while True:
        for i in m:
            if i in s:
                s.remove(i)
            else:
                f = True
                break

        if f:
            break

        c += 1

    print(c)