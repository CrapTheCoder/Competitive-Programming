n, a, b, c = map(int, input().split())
dp = [-1] * (n+1)
dp[0] = 0
 
for i in range(n+1):
    if dp[i] != -1:
        if i+a <= n: dp[i+a] = max(dp[i+a], dp[i]+1)
        if i+b <= n: dp[i+b] = max(dp[i+b], dp[i]+1)
        if i+c <= n: dp[i+c] = max(dp[i+c], dp[i]+1)
        
print(dp[n])