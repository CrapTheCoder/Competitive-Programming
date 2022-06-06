MOD = 998244353
 
n = int(input())
 
if n == 1:
    print(10)
    exit()
 
a = [1] * (n-1)
a[0] = 20
 
for i in range(1, n-1):
    a[i] *= (a[i-1] * 10) + (9 * (pow(10, i, MOD)))
    a[i] %= MOD
 
a.reverse()
 
for i in range(n-1):
    a[i] *= 9
    a[i] %= MOD
 
a.append(10)
 
print(*a)