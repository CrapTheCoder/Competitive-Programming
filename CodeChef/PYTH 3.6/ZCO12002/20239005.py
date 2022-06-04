def bsv(it):
    l = 0
    u = x - 1

    if it < v[0]:
        return -1

    while l <= u:
        m = (u + l) // 2

        if it == v[m]:
            return m
        elif it < v[m]:
            u = m - 1
        else:
            l = m + 1

    return l - 1

def bsw(it):
    l = 0
    u = y - 1

    if it > w[u]:
        return -1

    while l <= u:
        m = (u + l) // 2

        if it == w[m]:
            return m
        elif it < w[m]:
            u = m - 1
        else:
            l = m + 1

    return l

n, x, y = map(int, input().split())

c = []

for i in range(n):
    c.append(list(map(int, input().split())))

v = sorted(list(map(int, input().split())))
w = sorted(list(map(int, input().split())))

ans = float('inf')

for s, e in c:
    vi = bsv(s)
    wi = bsw(e)

    if wi != -1 and vi != -1:
        ans = min(ans, w[wi] - v[vi] + 1)

print(ans)