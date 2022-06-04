from bisect import bisect_left

d = list(map(int, input().split()))

n, k = d[:2]
a, b = sorted(d[2:n+2]), sorted(d[n+2:])
c, d = a.copy(), b.copy()

for _ in range(k):
    x, y = a.pop(0), b.pop()

    a.insert(bisect_left(a, y), y)
    b.insert(bisect_left(b, x), x)

for _ in range(k):
    x, y = c.pop(), d.pop(0)

    c.insert(bisect_left(c, y), y)
    d.insert(bisect_left(d, x), x)

print(min(a[-1] + b[-1], c[-1] + d[-1]))