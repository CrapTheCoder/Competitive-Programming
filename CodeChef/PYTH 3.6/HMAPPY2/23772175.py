from math import gcd

for _ in range(int(input())):
    n, a, b, k = map(int, input().split())
    s1, s2 = n // a, n // b

    g = (a * b) // gcd(a,b)
    count = s1 + s2 - 2 * (n // g)

    print(['Lose', 'Win'][count >= k])