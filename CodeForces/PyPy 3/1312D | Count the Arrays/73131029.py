MOD = 998244353
 
def C(n, r):
    num = den = 1
 
    for i in range(r):
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD
 
    return (num * pow(den, MOD - 2, MOD)) % MOD
 
n, m = map(int, input().split())
 
ans = C(m, n - 1) * (n - 2) * pow(2, n - 3)
 
print(int(ans % MOD))