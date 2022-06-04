from sys import stdin
from bisect import bisect_right
input = stdin.readline

max_ = lambda x, y: x if x > y else y


def lis(a):
    n = len(a)
    INF = float('inf')
    d = [INF] * (n + 1)
    d[0] = -INF

    for i in range(n):
        j = bisect_right(d, a[i])
        if d[j - 1] <= a[i] < d[j]:
            d[j] = a[i]

    ans = 0
    for i in range(n + 1):
        if d[i] < INF:
            ans = i

    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    c = a[:k]

    for i in range(k, n):
        for j in range(len(c), -1, -1):
            b = c[:j] + [a[i]] + c[j:]
            if lis(b) == k:
                c = b
                break

    if lis(c) != k or sorted(c) != a:
        print(-1)
    else:
        print(*c)