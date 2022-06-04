from bisect import insort
from math import nan

for _ in range(int(input())):
    n, x, p, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    total = 0

    p -= 1
    k -= 1

    if x not in a:
        total += 1

        a.pop(k)
        insort(a, x)

    if x < a[p]:
        a = [-i for i in a][::-1]
        k, p, x = -k-1, -p-1, -x

    reached = False

    for _ in range(n+1):
        if a[p] == x:
            reached = True
            print(total)
            break

        total += 1
        a.pop(k)
        a.append(nan)

    if not reached:
        print(-1)
