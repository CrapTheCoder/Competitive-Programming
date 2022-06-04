def binsearch(a, n, x):
    if n == 0:
        return 0

    l, r = 0, n - 1

    while l < r:
        m = (l + r) // 2

        if a[m] == x:
            return m

        if a[m] < x: l = m + 1
        if a[m] > x: r = m

    if a[l] < x:
        return l + 1

    return l

n, m = map(int, input().split())
a = []
l = 0

for _ in range(n + m):
    x = int(input())

    if x == -1:
        if l > 0:
            l -= 1
            print(a.pop())
    else:
        a.insert(binsearch(a, l, x), x)
        l += 1
