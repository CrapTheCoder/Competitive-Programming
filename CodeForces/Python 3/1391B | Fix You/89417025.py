for _ in range(int(input())):
n, m = map(int, input().split())

l = [input() for _ in range(n)]
c = 0

for i in range(n-1):
if l[i][-1] != 'D':
c += 1

for j in range(m-1):
if l[-1][j] != 'R':
c += 1

print(c)