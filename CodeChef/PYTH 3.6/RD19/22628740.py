def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = a[0]

    for i in a[1:]:
        r = gcd(i, r)

    print(0 - (r != 1))