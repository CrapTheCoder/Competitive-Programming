def check(p, q):
    x = y = 0
    ax = 0

    for i in s:
        if i == '0':
            ax ^= 1

        if ax == 0:
            if x < p:
                x += 1
            else:
                x -= 1
        else:
            if y < q:
                y += 1
            else:
                y -= 1

    if (x, y) == (p, q):
        return True

for _ in range(int(input())):
    n, p, q = map(int, input().split())
    s = input().strip()

    if check(p, q) or check(q, p):
        print('YES')
    else:
        print('NO')