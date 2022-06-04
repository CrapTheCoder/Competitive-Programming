def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a + b - gcd(a, b))