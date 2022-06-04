n = int(input())

i = j = x = y = 0

a = list(map(int, input().split()))
b = a.copy()

if n < 3:
    print(min(a[0], a[1]))
    exit()

a[1] += a[0]
a[2] += a[0]

for i in range(3, n):
    a[i] += min(a[i - 1], a[i - 2])

x = min(a[n - 1], a[n - 2])

b[0] += b[n - 1]
b[1] += b[n - 1]

for i in range(2, n - 1):
    b[i] += min(b[i - 1], b[i - 2])

y = min(b[n - 2], b[n - 3])

print(min(x, y))