from math import sqrt

n, k, r = map(int, input().split())
s = k // r

print(n - int((-1 + sqrt(1 + 8 * s)) / 2))
