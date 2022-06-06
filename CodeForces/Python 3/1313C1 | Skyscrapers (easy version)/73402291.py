n = int(input())
a = list(map(int, input().split()))

m = -1
mb = []

for mi in range(n):
b = [-1] * n
b[mi] = a[mi]

for i in range(mi-1, -1, -1):
if a[i] > b[i+1]:
b[i] = b[i+1]
else:
b[i] = a[i]

for i in range(mi+1, n):
if a[i] > b[i-1]:
b[i] = b[i-1]
else:
b[i] = a[i]

if m < sum(b):
m = sum(b)
mb = b

print(*mb)