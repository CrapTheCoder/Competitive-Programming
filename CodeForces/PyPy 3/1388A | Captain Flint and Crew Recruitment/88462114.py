d = [6, 10, 14]
s = sum(d)

for _ in range(int(input())):
n = int(input())

if n <= s:
print('NO')
continue

if n - s in d:
print('YES')
print(6, 10, 15, n-(6+10+15))
continue

else:
print('YES')
print(6, 10, 14, n-s)