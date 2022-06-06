for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))
c = {}

for j, i in enumerate(a):
c[i] = c.get(i, []) + [j+1]

x = list(c.values())

if len(x) == 1:
print('NO')
continue

print('YES')
s = x[0].pop(0)

for i in x[1]:
print(s, i)

for i in range(len(x)):
if i == 1:
continue

for j in x[i]:
print(x[1][0], j)