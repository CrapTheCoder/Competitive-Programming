from math import sqrt

INF = float('inf')

def divs(n):
    d = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            d.append(i)

            if n // i != i:
                d.append(n // i)

    return d

for _ in range(int(input())):
    h, x, y = map(int, input().split())
    h -= 1

    d = divs(h)

    mini = INF

    for i in d:
        if i - x >= 0 and (i - x) % y == 0:
            f = (i - x) // y + h // i

            mini = min(mini, f)

    if mini == INF:
        print(-1)
    else:
        print(mini)