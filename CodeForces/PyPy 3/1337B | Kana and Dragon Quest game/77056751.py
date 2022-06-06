for _ in range(int(input())):
x, n, m = map(int, input().split())

while x // 2 + 10 < x and n > 0:
n -= 1
x = x // 2 + 10

x -= 10 * m

if x > 0:
print('NO')
else:
print('YES')