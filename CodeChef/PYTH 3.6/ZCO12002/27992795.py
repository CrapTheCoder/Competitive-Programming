def binarySearch1(d):
    l = 0
    r = x - 1

    if d < v[0]:
        return -1

    while l <= r:
        m = (l + r) // 2

        if d == v[m]:
            return m
        elif d < v[m]:
            r = m - 1
        else:
            l = m + 1

    return l - 1

def binarySearch2(d):
    l = 0
    r = y - 1

    if d > w[r]:
        return -1

    while l <= r:
        m = (l + r) // 2

        if d == w[m]:
            return m
        elif d < w[m]:
            r = m - 1
        else:
            l = m + 1

    return l

n, x, y = map(int, input().split())

se = []

for i in range(n):
    se.append(tuple(map(int, input().split())))

v = sorted(list(map(int, input().split())))
w = sorted(list(map(int, input().split())))

m = float('inf')

for s, e in se:
    f, g = binarySearch1(s), binarySearch2(e)

    if f != -1 and g != -1:
        m = min(m, w[g] - v[f] + 1)

print(m)
