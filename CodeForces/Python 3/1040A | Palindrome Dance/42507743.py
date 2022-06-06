import math

n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

money = 0

for i in range(math.ceil(n / 2)):
x, y = arr[i] == 2, arr[n - i - 1] == 2

if x and y:
z = i == n - i - 1
money += min(a, b) * (2 - z)
continue
if x:
money += [a, b][arr[n - i - 1]]
if y:
money += [a, b][arr[i]]
if (not x and not y) and arr[i] != arr[n - i - 1]:
print(-1)
break
else:
print(money)