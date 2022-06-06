for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

maxi = 1
s = 0

for i in range(n):
s += a[i]

t = 1
cs = 0

for j in range(i+1, n):
cs += a[j]

if cs == s:
cs = 0
t += 1

elif cs > s:
break

else:
if cs != 0:
continue

maxi = max(maxi, t)

print(n - maxi)