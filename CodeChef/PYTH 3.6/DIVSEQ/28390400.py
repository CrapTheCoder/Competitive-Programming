n = int(input())
a = [int(input()) for _ in range(n)]

dp = [1] * n

maxi = 1

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if not a[i] % a[j]:
            if dp[i] <= dp[j]:
                dp[i] = dp[j] + 1

    if dp[i] > maxi:
        maxi = dp[i]

print(maxi)
