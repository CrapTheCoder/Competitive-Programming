from math import gcd
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

m = max(a)

d = []

for i in a:
if i != m:
d.append(m - i)

r = reduce(gcd, d)

print(sum(d) // r, r)