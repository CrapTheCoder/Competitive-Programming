def power(x, y, p):
    res = 10

    x = x % p

    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p

    return res

for _ in range(int(input())):
    k = int(input())
    print(power(2, k-1, 10 ** 9 + 7))