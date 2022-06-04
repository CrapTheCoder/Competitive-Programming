from sys import stdin
input = stdin.readline

from bisect import bisect_right

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {i: [] for i in a}

    for i, j in enumerate(a):
        d[j].append(i)

    ans = 1

    l = tuple(r[1] for r in sorted(d.items()))
    p = 0

    for i in range(len(l) - 1):
        x = bisect_right(l[i+1], l[i][p])

        if x == len(l[i+1]):
            ans += 1
            p = 0
        else:
            p = x

    print(ans)
