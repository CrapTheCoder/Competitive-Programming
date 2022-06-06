from sys import stdin, stdout
 
input = stdin.readline
 
MOD = 998244353
 
n, k = map(int, input().split())
p = list(map(int, input().split()))
 
d = {}
 
for i in range(n):
    d[p[i]] = i
 
l = [0] * k
s = 0
 
for i in range(n, n - k, -1):
    s += i
    l[n - i] = d[i]
 
l.sort()
 
f = 1
 
for i in range(1, k):
    f *= l[i] - l[i-1]
    f %= MOD
 
stdout.write(f'{s} {f}')