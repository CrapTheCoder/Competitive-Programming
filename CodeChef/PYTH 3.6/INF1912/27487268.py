from math import gcd

for _ in range(int(input())):
    n, k = map(int, input().split())

    rl = [0] * n
    cl = [0] * n

    for i in range(k):
        r, c = map(int, input().split())
        r -= 1
        c -= 1

        rl[r] += 1
        cl[c] += 1

    x = rl.count(0) * cl.count(0)
    g = gcd(x, n * n)

    print(x // g, n * n // g)

