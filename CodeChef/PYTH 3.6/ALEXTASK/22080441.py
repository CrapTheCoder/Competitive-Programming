def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = float('inf')

    for i in range(n):
        for j in range(i+1, n):
            c = lcm(a[i], a[j])

            if c < m:
                m = c

    print(m)
