MOD = 10 ** 9 + 7

for _ in range(int(input())):
    s, m = map(int, input().split())

    coins = list(map(int, input().split()))
    count = list(map(int, input().split()))

    dp = [[0] * (m+1) for _ in range(s+1)]
    dp[0] = [1] * (m+1)

    for i in range(1, s+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i][j - 1]

            for k in range(1, count[j-1] + 1):
                if i - coins[j - 1] * k >= 0:
                    dp[i][j] += dp[i - coins[j - 1] * k][j-1]

    print(dp[-1][-1] % MOD)