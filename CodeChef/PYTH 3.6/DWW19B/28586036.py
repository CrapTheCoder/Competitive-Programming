from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    m = min(lcm(k, i) for i in a)

    if m > 10 ** 18:
        print(-1)
    else:
        print(m)
    