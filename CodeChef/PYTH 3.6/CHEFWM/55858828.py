for _ in range(int(input())):
    n, m = map(int, input().split())
    om = m

    if m == 1:
        print(0)
        continue

    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            break
    else:
        print(1)
        continue

    c = 0
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            c += 1
            while m % i == 0:
                m //= i

    if m > 1:
        c += 1

    maxi = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if c >= i:
                maxi = max(maxi, i)

            if c >= n // i:
                maxi = max(maxi, n // i)

    print(maxi)
