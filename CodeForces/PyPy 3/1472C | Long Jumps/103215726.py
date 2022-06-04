for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    dp = [0] * n
    for i in range(n-1, -1, -1):
        dp[i] = a[i]
 
        if i + a[i] < n:
            dp[i] += dp[i + a[i]]
 
    print(max(dp))