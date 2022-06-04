MOD = 998244353

def inv(i):
    return pow(i, MOD-2, MOD)

for _ in range(int(input())):
    n = int(input())
    s = n * (n+1) // 2
    t = n * (n-1) // 2

    print((n * (n+1) ** 2) % MOD * inv(4) % MOD)
