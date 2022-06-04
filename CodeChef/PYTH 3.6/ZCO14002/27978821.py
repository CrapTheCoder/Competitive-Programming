n = int(input())
a = list(map(int, input().split()))

if n < 3:
    print(0)
    exit()

dp = [[float('inf')] * 3 for _ in range(n)]

dp[0] = [a[0]] * 3
dp[1] = [a[0] + a[1], a[1], a[1]]
dp[2] = [a[1] + a[2], a[0] + a[2], a[2]]

for i in range(3, n):
    dp[i][0] = min(dp[i - 1]) + a[i]
    dp[i][1] = min(dp[i - 2]) + a[i]
    dp[i][2] = min(dp[i - 3]) + a[i]

print(min(min(dp[-1]), min(dp[-2]), min(dp[-3])))