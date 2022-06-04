from functools import reduce
from math import sqrt

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if not n % i)))

INF = float('inf')

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}

    maxi = -1

    for i in a:
        p = factors(i)
        m = INF

        for j in list(p):
            d[j] = d.get(j, 0) + 1
            m = min(d[j], m)

        m -= 1

        if maxi < m:
            maxi = m

    print(maxi)