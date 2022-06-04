from math import sqrt

def divs(n):
    a = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            a.append(i)

            if n // i != i:
                a.append(n // i)

    return a

for _ in range(int(input())):
    c, d = map(int, input().split())

    a = sorted(divs(min(c, d)), reverse=True)

    for i in a:
        if c % i == d % i == 0:
            print((c // i) * (d // i))
            break
