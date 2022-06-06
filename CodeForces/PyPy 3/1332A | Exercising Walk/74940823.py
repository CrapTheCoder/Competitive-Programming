for _ in range(int(input())):
a, b, c, d = map(int, input().split())
x, y, x1, y1, x2, y2 = map(int, input().split())

if x1 == x == x2 and (a or b):
print('No')
continue

if y1 == y == y2 and (c or d):
print('No')
continue

d0 = min(a, b, c, d)

a -= d0
b -= d0
c -= d0
d -= d0

d1 = min(a, b)

a -= d1
b -= d1

d2 = min(c, d)

c -= d2
d -= d2

a = -a
c = -c

if x1 <= x + (a + b) <= x2 and y1 <= y + (c + d) <= y2:
print('Yes')
else:
print('No')