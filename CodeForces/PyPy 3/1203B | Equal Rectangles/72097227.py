for _ in range(int(input())):
n = int(input())
a = sorted(map(int, input().split()))

x = []

for i in range(len(a)):
x.append(a[i] * a[len(a) - i - 1])

if len(set(x)) == 1 and a[::2] == a[1::2]:
print('YES')
else:
print('NO')