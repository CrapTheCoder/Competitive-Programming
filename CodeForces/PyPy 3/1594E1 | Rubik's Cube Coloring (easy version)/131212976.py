MOD = 10 ** 9 + 7
n = int(input())
 
f = 6
 
for i in range(1, n):
    f = (f * pow(4, 2 ** i, MOD)) % MOD
 
print(f % MOD)