for _ in range(int(input())):
n, x, a, b = map(int, input().split())

if b < a:
a, b = b, a

while a != 1 and x != 0:
a -= 1
x -= 1

while b != n and x != 0:
b += 1
x -= 1

print(b - a)