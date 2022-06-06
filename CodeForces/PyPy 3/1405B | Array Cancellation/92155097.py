for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

s = 0

for i in range(n-1, -1, -1):
if a[i] < 0:
s += abs(a[i])

else:
s = max(s - a[i], 0)

print(s)