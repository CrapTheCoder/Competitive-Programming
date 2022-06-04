for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = []

    s = 0

    for i in a[:-1]:
        if i <= k:
            s += i
        else:
            b.append(i-k)

    s += len(b) * k + a[-1]

    if not b:
        print(s)
        continue

    if sum(b[:-1]) <= b[-1]:
        s -= b[-1] - sum(b[:-1])
    else:
        s -= sum(b) % 2

    print(s)