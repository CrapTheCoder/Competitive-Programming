n, k = map(int, input().split())

l = [1]

c = 0

for i in range(k, 1, -1):
if c % 2 == 0: l.append(l[-1] + i)
if c % 2 == 1: l.append(l[-1] - i)

c += 1

s = sorted(set(range(1, n + 1)).difference(set(l)))

l.extend(s)

print(*l)