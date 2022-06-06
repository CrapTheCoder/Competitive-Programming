from sys import stdin

input = stdin.readline

for _ in range(int(input())):
n = int(input())

g = []

used = set()

x = set()

for i in range(n):
l = set(list(map(int, input().split()))[1:]).difference(used)

if l:
used.add(sorted(l)[0])
else:
x.add(i)

if x:
print('IMPROVE')

for x in x: break
for y in set(range(1, n + 1)).difference(used): break

print(x+1, y)
else:
print('OPTIMAL')