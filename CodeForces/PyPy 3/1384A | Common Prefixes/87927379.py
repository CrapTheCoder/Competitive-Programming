from string import ascii_lowercase as alps

for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))
m = max(a + [1])

l = [[''] * m for _ in range(n+1)]

for i in range(m):
l[0][i] = alps[i % 26]

for i in range(1, n+1):
c = a[i-1]
l[i][:c] = l[i-1][:c]

if c != m:
x = alps.index(l[i-1][c]) + 1

for j in range(c, m):
l[i][j] = alps[x % 26]
x += 1

for i in l:
print(*i, sep='')