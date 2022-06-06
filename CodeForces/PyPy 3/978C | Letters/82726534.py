n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p = [0]

for i in a:
p.append(p[-1] + i)

cur = 1

for i in b:
while i > p[cur]:
cur += 1

print(cur, i - p[cur - 1])