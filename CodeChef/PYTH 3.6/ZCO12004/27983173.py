n = int(input())
a = list(map(int, input().split()))

dp1 = [float('inf') for _ in range(n)]
dp2 = [float('inf') for _ in range(n)]

dp1[0], dp1[1] = a[0], a[1]
dp2[-1], dp2[-2] = a[-1], a[-2]

for i in range(2, n):
    dp1[i] = min(dp1[i-1], dp1[i-2]) + a[i]

for i in range(n-3, -1, -1):
    dp2[i] = min(dp2[i+1], dp2[i+2]) + a[i]

print(min(dp1[-1], dp2[0]))