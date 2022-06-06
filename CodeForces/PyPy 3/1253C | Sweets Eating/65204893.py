n, m = map(int, input().split())
a = sorted(map(int, input().split()))

l = [a[0]]
y = [0] * m
y[0] = a[0]

for i in range(1, m):
l.append(l[-1] + a[i])
y[i] = a[i]

for i in range(m, n):
x = l[-1]

y[i % m] += a[i]

if i - m >= 0:
x += y[i % m]

l.append(x)

print(*l)
