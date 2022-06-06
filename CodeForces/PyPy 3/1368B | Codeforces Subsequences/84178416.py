from functools import reduce

n = int(input())
s = 'codeforces'

c = [0] * len(s)
ci = 0

while reduce(int.__mul__, c) < n:
c[ci] += 1
ci += 1
ci %= len(s)

x = ''

for j, i in enumerate(s):
print(i * c[j], end='')