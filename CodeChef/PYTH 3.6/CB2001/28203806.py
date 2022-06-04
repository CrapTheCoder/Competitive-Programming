d = {}

def gcd(a, b):
    if (a, b) in d:
        return d[a, b]

    d[a, b] = gcd(b, a % b) if b != 0 else a
    return d[a, b]

def lcm(a, b):
    return (a * b) // gcd(a, b)

for _ in range(int(input())):
    n = int(input())

    s = 0

    for i in range(1, n + 1):
        s = (s + lcm(n, i)) % 1000000007

    print(s // n)
