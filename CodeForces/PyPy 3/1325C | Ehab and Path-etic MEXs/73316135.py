from sys import stdin

input = stdin.readline

n = int(input())

d = [0] * n
uv = []

for _ in range(n - 1):
u, v = map(int, input().split())

u -= 1
v -= 1

d[u] += 1
d[v] += 1

uv.append((u, v))

i = j = -1

for i, j in enumerate(d):
if j >= 3:
break

c1 = 0
c2 = n - 2

for u, v in uv:
if u == i or v == i:
print(c1)
c1 += 1
else:
print(c2)
c2 -= 1