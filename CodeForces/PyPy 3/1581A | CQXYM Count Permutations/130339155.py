MOD = 10 ** 9 + 7
 
for _ in range(int(input())):
    n = int(input())
 
    f = 1
    for i in range(1, 2*n+1):
        f *= i
        f %= MOD
 
    print(f * pow(2, MOD - 2, MOD) % MOD)