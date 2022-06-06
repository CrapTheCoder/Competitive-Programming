for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

l1 = [False] * n
l2 = [False] * n

for i in range(n):
l1[i] = i <= a[i]
if i > 0: l1[i] = l1[i] and l1[i-1]

for i in range(n-1, -1, -1):
l2[i] = n-i-1 <= a[i]
if i < n - 1: l2[i] = l2[i] and l2[i+1]

if any(l1[i] and l2[i] for i in range(n)) or l1[-1] or l2[0]:
print('Yes')
else:
print('No')