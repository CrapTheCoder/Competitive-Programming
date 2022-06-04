n, k = map(int, input().split())
a = list(map(int, input().split()))

s = sum((1 / a[i]) * (a[i] * (a[i] + 1) // 2) for i in range(k))

m = s

for i in range(k, n):
    s += (1 / a[i]) * (a[i] * (a[i] + 1) // 2)

    i -= k

    s -= (1 / a[i]) * (a[i] * (a[i] + 1) // 2)

    m = max(m, s)

print('%.12f'%m)