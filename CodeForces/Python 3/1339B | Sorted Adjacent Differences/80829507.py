for _ in range(int(input())):
n = int(input())
a = sorted(map(int, input().split()))

b = []

for i in range(n // 2):
b.append(a[i])
b.append(a[n-i-1])

if n % 2:
b.append(a[n // 2])

b.reverse()

print(*b)