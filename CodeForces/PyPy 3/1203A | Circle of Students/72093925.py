for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

s1 = list(range(1, n + 1))
s2 = list(range(1, n + 1))[::-1]

for i in range(n):
if a == s1 or a == s2:
print('YES')
break

a = a[1:] + [a[0]]

else:
print('NO')