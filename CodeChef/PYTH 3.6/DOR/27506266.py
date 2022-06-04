def solvepos(n):
    x = -1

    while n:
        n = n >> 1
        x += 1

    return x


def solve(l, r):
    a = 0

    x = solvepos(l)
    y = solvepos(r)

    while x == y:
        d = (1 << x)

        a += d

        l -= d
        r -= d

        x = solvepos(l)
        y = solvepos(r)

    x = max(x, y)

    for i in range(x, -1, -1):
        d = (1 << i)
        a += d

    return a


g = {}

for _ in range(int(input())):
    l, r = map(int, input().split())

    if (l, r) in g:
        print(g[(l, r)])
    else:
        if l == r:
            g[(l, r)] = l
            print(l)
        else:
            x = solve(l, r)
            g[(l, r)] = x
            print(x)