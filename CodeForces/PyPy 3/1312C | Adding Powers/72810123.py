def f(n):
d = []

while n != 0:
x, y = divmod(n, k)

d.append(y)
n = x

return d

for _ in range(int(input())):
n, k = map(int, input().split())
a = list(map(int, input().split()))

l = {}

for i in a:
x = f(i)

for j in range(len(x)):
if x[j] > 0:
l[j] = l.get(j, 0) + x[j]

if any(l[i] != 1 for i in l):
print('NO')
else:
print('YES')