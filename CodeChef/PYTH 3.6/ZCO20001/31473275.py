def log_(n):
    x, c = 1, 0

    while True:
        x *= 2

        if x > n:
            break

        c += 1

    return c

for _ in range(int(input())):
    p, idx = map(int, input().split())

    ans = 0

    while idx > 0:
        d = log_(idx)
        ans += pow(2, p - d - 1)
        idx -= pow(2, d)

    print(ans)
