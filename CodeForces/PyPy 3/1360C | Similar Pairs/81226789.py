for _ in range(int(input())):
n = int(input())
a = sorted(map(int, input().split()))

odd = even = 0

for i in a:
if i % 2 == 1:
odd += 1
else:
even += 1

if odd % 2 == even % 2 == 0:
print('YES')
continue

if odd % 2 != even % 2:
print('NO')
continue

cnt = 0

for i in range(1, n):
if a[i-1] == a[i] - 1:
cnt += 1

print('YES' if cnt >= 1 else 'NO')