for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))
m = max(a)

for i in range(n):
if i-1 >= 0:
if a[i-1] != a[i] and a[i] == m:
print(i+1)
break

if i + 1 < n:
if a[i+1] != a[i] and a[i] == m:
print(i+1)
break

else:
print(-1)