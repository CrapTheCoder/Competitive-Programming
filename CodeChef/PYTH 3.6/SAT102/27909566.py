for _ in range(int(input())):
    n, m = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * m for _ in range(n)]

    dp[0][0] = t[0][0]

    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue

            if i - 1 < 0:
                dp[i][j] = dp[i][j-1] + t[i][j]
            elif j - 1 < 0:
                dp[i][j] = dp[i-1][j] + t[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + t[i][j]

    print(dp[n-1][m-1])
