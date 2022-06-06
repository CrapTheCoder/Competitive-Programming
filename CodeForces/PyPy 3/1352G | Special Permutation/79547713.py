for _ in range(int(input())):
n = int(input())

x1 = []

for i in range(1, n + 1, 4):
x1.append(i)

x2 = []

for i in range(2, n + 1, 4):
x2.append(i)

x3 = []

for i in range(3, n + 1, 4):
x3.append(i)

x4 = []

for i in range(4, n + 1, 4):
x4.append(i)

x = x3 + x1[::-1] + x4 + x2[::-1]

for i in range(1, n):
if not 2 <= abs(x[i] - x[i-1]) <= 4:
print(-1)
break
else:
print(*x)