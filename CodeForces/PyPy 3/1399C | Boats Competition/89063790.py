for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

d = {}

for i in range(n):
for j in range(i+1, n):
cs = a[i] + a[j]
d[cs] = d.get(cs, set())

if (i in d[cs]) or (j in d[cs]):
continue

d[cs].add(i)
d[cs].add(j)

if d:
print(max(len(d[i]) for i in d) // 2)
else:
print(0)