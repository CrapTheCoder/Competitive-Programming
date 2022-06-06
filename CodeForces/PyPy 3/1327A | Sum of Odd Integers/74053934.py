for _ in range(int(input())):
n, k = map(int, input().split())

if n % 2 != k % 2:
print('NO')
else:
if k ** 2 <= n:
print('YES')
else:
print('NO')