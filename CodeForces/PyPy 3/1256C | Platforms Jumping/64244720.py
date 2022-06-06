n, m, d = map(int, input().split())
a = list(map(int, input().split()))

l = [0] * (n * 2)
ci = d - 1

for i in range(m):
l[ci:ci+a[i]] = [i + 1] * a[i]

if ci >= n:
for _ in range(ci - n + 1):
l.remove(0)

ci = n + a[i] - 1
else:
ci += a[i] - 1 + d

for i in range(ci - n):
l.remove(0)

if ci < n:
print('NO')
else:
print('YES')
print(*l[:n])