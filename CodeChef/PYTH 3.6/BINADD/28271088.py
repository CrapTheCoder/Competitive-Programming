def solve(a, b):
    if b == '0':
        return 0

    a = '0' + a
    b = '0' + b

    n = len(a)
    m = len(b)

    if m > n:
        a = a.zfill(m)
        n = m

    else:
        b = b.zfill(n)

    m = 0
    v1 = v2 = 0

    for i in range(1, n):
        if a[i] == b[i] == '1':
            m = max(v1 + 1, v2 + 1, m)

            v1 = v2 = 0

        elif a[i] == b[i] == '0':
            v1 = v2 = 0

        else:
            v1 += 1
            v2 += 1

    return m + 1

for _ in range(int(input())):
    a = input()
    b = input()

    print(solve(a, b))
