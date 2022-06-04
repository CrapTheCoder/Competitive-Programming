from math import gcd

n, c = map(int, input().split())
a = list(map(int, input().split()))

g = a[0] - c

for i in range(1, n):
    g = gcd(g, a[i] - a[i-1])

print(g)