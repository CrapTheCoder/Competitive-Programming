t = int(input())

for _ in range(t):
n = int(input())
s = input()

m = []
d = [[], []]
c = 0

for i in s:
i = int(i)

if i == 0:
if d[1]:
x = d[1].pop()
d[0].append(x)
m.append(x)

else:
c += 1
d[0].append(c)
m.append(c)

else:
if d[0]:
x = d[0].pop()
d[1].append(x)
m.append(x)

else:
c += 1
d[1].append(c)
m.append(c)

print(len(set(m)))
print(*m)