from math import gcd
from sys import stdin
input = stdin.readline
 
def lcm(x, y):
    return x * y // gcd(x, y)
 
for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
 
    c = s * (lcm(len(s), len(t)) // len(s))
    d = t * (lcm(len(s), len(t)) // len(t))
 
    if c == d:
        print(c)
    else:
        print(-1)