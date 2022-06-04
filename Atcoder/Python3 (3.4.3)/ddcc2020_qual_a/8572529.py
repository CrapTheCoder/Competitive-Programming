x, y = map(int, input().split())
x -= 1
y -= 1

d = [300000, 200000, 100000]

if x == y == 0:
    print(d[x] + d[y] + 400000)
else:
    s = 0

    if x < 3:
        s += d[x]
    if y < 3:
        s += d[y]

    print(s)