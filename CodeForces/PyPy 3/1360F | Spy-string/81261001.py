for _ in range(int(input())):
n, m = map(int, input().split())
a = [input() for _ in range(n)]

cns = [([0] * n, '')]

for j in range(m):
d = {}

for i in range(n):
d[a[i][j]] = d.get(a[i][j], []) + [i]

ncns = []

for c in d:
for cn, cur in cns:
nc = cn.copy()

for i in range(n):
nc[i] += 1

for x in d[c]:
nc[x] -= 1

if 2 in nc:
continue

ncns.append((nc, cur + c))

cns = ncns

if not cns:
print(-1)
else:
print(cns[0][1])