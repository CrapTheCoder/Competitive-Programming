for _ in range(int(input())):
    s = list(input())
    a = b = c = 0
    p = 'C'

    for i in s:
        if i == 'A':
            a += 1
            if p == 'A': a += c
            c, p = 0, 'A'

        elif i == 'B':
            b += 1
            if p == 'B': b += c
            c, p = 0, 'B'

        else: c += 1

    print(a, b)