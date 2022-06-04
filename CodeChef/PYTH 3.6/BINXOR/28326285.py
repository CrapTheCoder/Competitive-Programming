MOD = 10 ** 9 + 7

length = 10 ** 5 + 1

ifacts = [-1] * (length + 1)
infacts = [-1] * (length + 1)

fact = [-1] * (length + 1)

fact[0] = 1

for i in range(1, length + 1):
    fact[i] = (fact[i - 1] * i) % MOD

infacts[0] = infacts[1] = 1

for i in range(2, length + 1, 1):
    infacts[i] = (infacts[MOD % i] * (MOD - int(MOD / i)) % MOD)

ifacts[0] = ifacts[1] = 1

for i in range(2, length + 1, 1):
    ifacts[i] = (infacts[i] * ifacts[i - 1]) % MOD

def ncr(n, r):
    ans = ((fact[n] * ifacts[r]) % MOD * ifacts[n - r]) % MOD

    return ans

for _ in range(int(input())):
    n = int(input())

    a = input()
    b = input()

    x, y = a.count('1'), b.count('1')

    s = 0

    for r in range(abs(x - y), ((x + y) if (x + y) <= n else 2 * n - x - y) + 1, 2):
        s += ncr(n, r)
        s %= MOD

    print(s)
