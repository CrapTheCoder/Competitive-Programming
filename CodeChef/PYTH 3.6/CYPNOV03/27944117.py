n, m = map(int, input().split())
a = [-1] * n

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    while a[x] >= 0: x = a[x]
    while a[y] >= 0: y = a[y]

    if x != y:
        if a[x] > a[y]:
            x, y = y, x

        a[x] += a[y]
        a[y] = x

print(sum(i < 0 for i in a))