MOD = 1000000007

l = [1]
n = 1000000

m = f = 1

for i in range(2, n+1):
    f = (f * i) % MOD
    m = (m * f) % MOD

    l.append(m)

for _ in range(int(input())):
    n = int(input())
    print(l[n-1])
