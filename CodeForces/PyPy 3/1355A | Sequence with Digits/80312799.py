for _ in range(int(input())):
n, k = input().split()
k = int(k)

for i in range(k-1):
x, y = min(n), max(n)
x = int(x)
y = int(y)

if x == 0 or y == 0:
break

n = str(int(n) + x * y)

print(n)