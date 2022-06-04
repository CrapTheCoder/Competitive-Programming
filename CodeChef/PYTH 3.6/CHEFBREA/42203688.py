from math import gcd

for _ in range(int(input())):
    l, b = map(int, input().split())
    g = gcd(l, b)

    print((l // g) * (b // g))