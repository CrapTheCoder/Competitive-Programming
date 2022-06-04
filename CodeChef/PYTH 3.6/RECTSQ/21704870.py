def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for i in range(int(input())):
    n, m = map(int, input().split())
    print(n * m // (gcd(n, m) ** 2))