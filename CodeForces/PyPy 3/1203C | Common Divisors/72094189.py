from math import gcd, sqrt
from functools import reduce

def divs(n):
c = 0

for i in range(1, int(sqrt(n)) + 1):
if n % i == 0:
c += 1

if n // i != i:
c += 1

return c

n = int(input())
a = list(map(int, input().split()))

g = reduce(gcd, a)

print(divs(g))