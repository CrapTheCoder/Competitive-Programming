def solve(s, n):
    dp = [[0] * n for _ in range(n)]

    ml = 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n-1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ml = 2

        i += 1

    k = 3

    while k <= n:
        i = 0

        while i < (n - k + 1):
            j = i + k - 1

            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if k > ml: ml = k

            i += 1

        k += 1

    return ml

n, s = input().split()
n = int(n)

print(solve(s, n))