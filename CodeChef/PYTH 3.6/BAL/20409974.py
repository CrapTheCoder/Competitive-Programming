def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

for _ in range(int(input())):
    x, y, n, m = map(int, input().split())

    l = lcm(x, y)

    print('YES' if (l // x) <= n and (l // y) <= m else 'NO')
