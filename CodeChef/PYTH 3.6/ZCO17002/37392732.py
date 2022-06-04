inp = list(map(int, input().split()))

n, m, w, b = map(int, inp[:4])

ws = []
bs = []

for i in range(w): ws.append(tuple(map(int, inp[4+i*2:4+i*2+2])))
for i in range(w, w+b): bs.append(tuple(map(int, inp[4+i*2:4+i*2+2])))

d = {}

for x, y in ws: d[x] = d.get(x, []) + [(y, 'W')]
for x, y in bs: d[x] = d.get(x, []) + [(y, 'B')]

t = 0

for k in range(1, n+1):
    a = d.get(k, [])
    f = 0

    a = [(0, 'N')] + sorted(a)
    r = len(a)

    for i in range(1, r):
        if a[i][1] == 'B':
            f += (a[i][0] - a[i-1][0]) * (a[i][0] - a[i-1][0] + 1) // 2 - 1

        if a[i][1] == 'W':
            if i + 1 < r:
                p1 = (a[i+1][0] - a[i-1][0]) * (a[i+1][0] - a[i-1][0] + 1) // 2 - 1
                p2 = (a[i+1][0] - a[i][0] + 1) * (a[i+1][0] - a[i][0] + 2) // 2 - 1

                f += p1 - p2

            else:
                p1 = (m - a[i-1][0]) * (m - a[i-1][0] + 1) // 2 - 1
                p2 = (m - a[i][0] + 1) * (m - a[i][0] + 2) // 2 - 1

                f += p1 - p2

    f += (m - a[-1][0]) * (m - a[-1][0] + 1) // 2

    t += f

print(t)
