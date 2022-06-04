from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

for _ in range(int(input())):
    x, y = map(int, input().split())

    print((lcm(x, y) // x - 1) + (lcm(x, y) // y - 1))