for _ in range(int(input())):
n = int(input())
a = sorted(list(map(int, input().split())))

m = -1

for i in range(n):
m = max(min(a[i], n - i), m)

print(m)