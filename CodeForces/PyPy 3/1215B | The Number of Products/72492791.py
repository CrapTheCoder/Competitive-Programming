n = int(input())
a = list(map(int, input().split()))

dp1 = [0] * n
dp2 = [0] * n

if 0 < a[0]: dp1[0] = 1
if 0 > a[0]: dp2[0] = 1

for i in range(1, n):
if 0 < a[i]:
dp1[i] = dp1[i-1] + 1
dp2[i] = dp2[i-1]

if 0 > a[i]:
dp1[i] = dp2[i-1]
dp2[i] = dp1[i-1] + 1

pos = sum(dp1)
neg = sum(dp2)

print(neg, pos)