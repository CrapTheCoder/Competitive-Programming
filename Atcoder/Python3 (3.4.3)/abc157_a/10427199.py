def ncr(n, r):
    num = den = 1

    for i in range(r):
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD

    return (num * pow(den, MOD - 2, MOD)) % MOD

MOD = 10 ** 9 + 7

n, a, b = map(int, input().split())

x = pow(2, n, MOD)

print((x - ncr(n, a) - ncr(n, b) - 1) % MOD)
