INF = float('inf')
 
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    dp = [[INF] * (2*n+1) for _ in range(n+1)]
 
    for j in range(2*n+1):
        dp[0][j] = 0
 
    for i in range(n):
        for j in range(2*n):
            dp[i+1][j+1] = min(dp[i][j] + abs(a[i] - (j+1)), dp[i+1][j])
 
    print(dp[-1][-1])