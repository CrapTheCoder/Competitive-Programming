for _ in range(int(input())):
n, m = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(lambda x: int(x) - 1, input().split()))

b = sorted(a)
c = a.copy()

while True:
for i in p:
if a[i] > a[i + 1]:
a[i], a[i + 1] = a[i + 1], a[i]

if a == b:
print('YES')
break

if a == c:
print('NO')
break

c = a.copy()