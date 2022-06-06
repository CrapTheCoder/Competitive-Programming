for _ in range(int(input())):
n, m, a, b = map(int, input().split())

t = 0

for i in range(n):
l = input()

u = 0

i = 0

while i < m:
if l[i] == '.':
if i < m-1 and l[i+1] == '.':
u += 1
else:
t += a

i += 2
continue

i += 1

if u * b > 2 * u * a:
t += 2 * u * a
else:
t += u * b

print(t)