from math import factorial

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    x = a.count(a[k-1])
    y = a[:k].count(a[k-1])

    print(factorial(x) // (factorial(y) * factorial(x - y)))
