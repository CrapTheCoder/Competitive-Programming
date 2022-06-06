for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

d = []

for i in range(n):
if a[i] == -1:
if i - 1 >= 0 and a[i - 1] != -1:
d.append(a[i - 1])

if i + 1 < n and a[i + 1] != -1:
d.append(a[i + 1])

rep = 0

if d:
rep = (min(d) + max(d)) // 2

for i in range(n):
if a[i] == -1:
a[i] = rep

maxi = -1

for i in range(1, n):
maxi = max(maxi, abs(a[i] - a[i-1]))

print(maxi, rep)