for _ in range(int(input())):
    x, q = map(int, input().split())

    for _ in range(q):
        f = int(input())

        if f == 1:
            i = int(input()) - 1

            if (x >> i) & 1:
                print('ON')
            else:
                print('OFF')

        elif f == 2:
            i = int(input()) - 1
            if not ((x >> i) & 1):
                x ^= 1 << i

        elif f == 3:
            i = int(input()) - 1
            if (x >> i) & 1:
                x ^= 1 << i

        elif f == 4:
            p, q = map(int, input().split())
            p -= 1
            q -= 1

            ox = x

            x -= ((ox >> p) & 1) * (1 << p)
            x += ((ox >> q) & 1) * (1 << p)
            x -= ((ox >> q) & 1) * (1 << q)
            x += ((ox >> p) & 1) * (1 << q)
