from math import gcd

for _ in range(int(input())):
    l, b = map(int, input().split())
    print(gcd(l, b))