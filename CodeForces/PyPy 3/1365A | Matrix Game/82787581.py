from sys import stdin
input = stdin.readline

for _ in range(int(input())):
n, m = map(int, input().split())

l = [[] for _ in range(m)]

r = c = 0

for _ in range(n):
a = list(map(int, input().split()))

for i in range(m):
l[i].append(a[i])

if 1 not in a:
r += 1

for a in l:
if 1 not in a:
c += 1

if min(r, c) % 2:
print('Ashish')
else:
print('Vivek')