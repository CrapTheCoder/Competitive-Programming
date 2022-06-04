from functools import reduce

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for _ in range(int(input())):
    l = list(map(int, input().split()))
    n, a = l[0], l[1:]

    x = reduce(gcd, a)

    print(*[i // x for i in a])