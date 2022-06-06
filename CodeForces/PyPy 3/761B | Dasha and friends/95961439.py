n, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(l):
for j in range(n):
a[j] = (a[j] + 1) % l

a.sort()

if a == b:
print('YES')
break
else:
print('NO')