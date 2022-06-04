from math import gcd

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x * y // gcd(x, y))