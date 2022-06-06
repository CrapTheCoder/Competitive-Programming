MOD = 10 ** 9 + 7
n = int(input())
 
f = 1
 
for i in range(1, n+1):
    f *= i
    f %= MOD
 
print((f - pow(2, n-1, MOD)) % MOD)