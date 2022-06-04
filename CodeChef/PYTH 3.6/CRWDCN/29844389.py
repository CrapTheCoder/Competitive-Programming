from math import gcd

def lcm(n, m):
    return n * m // gcd(n, m)

for _ in range(int(input())):
    n = int(input()) * 24

    x, y, z = map(int, input().split())

    a = lcm(lcm(x, y), z)

    print(n // a)