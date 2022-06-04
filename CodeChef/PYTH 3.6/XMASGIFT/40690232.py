from math import gcd

def lcm1(x, y):
    return x * y // gcd(x, y)

def lcm(a):
    l = 1
    for i in a:
        l = lcm1(l, i)

    return l

def f(x, *a):
    return x // lcm(a)

def count(x):
    return f(x, v1) + f(x, v2) + f(x, v3) + f(x, v4) + f(x, v5) \
           - f(x, v1, v2) - f(x, v1, v3) - f(x, v1, v4) - f(x, v1, v5) \
           - f(x, v2, v3) - f(x, v2, v4) - f(x, v2, v5) \
           - f(x, v3, v4) - f(x, v3, v5) \
           - f(x, v4, v5) \
           + f(x, v1, v2, v3) + f(x, v1, v2, v4) + f(x, v1, v2, v5) \
           + f(x, v1, v3, v4) + f(x, v1, v3, v5) \
           + f(x, v1, v4, v5) \
           + f(x, v2, v3, v4) + f(x, v2, v3, v5) \
           + f(x, v2, v4, v5) \
           + f(x, v3, v4, v5) \
           - f(x, v1, v2, v3, v4) \
           - f(x, v1, v2, v3, v5) \
           - f(x, v1, v2, v4, v5) \
           - f(x, v1, v3, v4, v5) \
           - f(x, v2, v3, v4, v5) \
           + f(x, v1, v2, v3, v4, v5) \

for _ in range(int(input())):
    n, m, a, d = map(int, input().split())
    v1, v2, v3, v4, v5 = a, a+d, a+2*d, a+3*d, a+4*d

    print((m - n + 1) - (count(m) - count(n-1)))
