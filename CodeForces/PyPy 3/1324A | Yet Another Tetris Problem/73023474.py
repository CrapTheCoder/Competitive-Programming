for _ in range(int(input())):
n = int(input())
a = sorted(map(int, input().split()))

x = a[0] % 2

if all(i % 2 == x for i in a):
print('YES')
else:
print('NO')