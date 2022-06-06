from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

m = max(c, key=c.get)

x = a.index(m)

print(n - c[m])

for i in range(x-1, -1, -1):
if a[i] == m:
continue

if a[i] < m:
print(1, i+1, i+2)
else:
print(2, i+1, i+2)

for i in range(x+1, n):
if a[i] == m:
continue

if a[i] < m:
print(1, i+1, i)
else:
print(2, i+1, i)