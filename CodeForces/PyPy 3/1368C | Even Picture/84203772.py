n = int(input())

l = [(0, 0)]

for i in range(1, n+2):
l.append((i, i))
l.append((i-1, i))
l.append((i, i-1))

print(len(l))

for i, j in l:
print(i, j)