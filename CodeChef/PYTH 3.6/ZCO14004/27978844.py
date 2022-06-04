n = int(input())
a = list(map(int, input().split()))

if n < 3:
    print(sum(a))
    exit()

dp = [-1] * n

dp[0] = a[0]
dp[1] = a[1]
dp[2] = a[2]

for i in range(3, n):
    dp[i] = min(dp[i-3:i]) + a[i]

print(sum(a) - min(dp[-3:]))