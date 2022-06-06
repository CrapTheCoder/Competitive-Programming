for _ in range(int(input())):
n, m = map(int, input().split())

flag = False

for _ in range(n):
a, b = input().split()
c, d = input().split()

if b == c:
flag = True

print('YES' if flag and (m % 2 == 0) else 'NO')