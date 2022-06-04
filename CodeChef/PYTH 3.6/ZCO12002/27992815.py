def binarySearch1(d):
    l, r = 0, x - 1

    if d < v[0]:
        return -1

    while l <= r:
        mid = (l + r) // 2

        if v[mid] == d:
            return mid
        elif v[mid] < d:
            l = mid + 1
        else:
            r = mid - 1

    return l - 1

def binarySearch2(d):
    l, r = 0, y - 1

    if d > w[r]:
        return -1

    while l <= r:
        mid = (l + r) // 2

        if w[mid] == d:
            return mid
        elif w[mid] < d:
            l = mid + 1
        else:
            r = mid - 1

    return l

n, x, y = map(int, input().split())

se = []

for _ in range(n):
    se.append(tuple(map(int, input().split())))

v = sorted(map(int, input().split()))
w = sorted(map(int, input().split()))

m = float('inf')

for s, e in se:
    f, g = binarySearch1(s), binarySearch2(e)

    if f != -1 and g != -1:
        m = min(m, w[g] - v[f] + 1)

print(m)
