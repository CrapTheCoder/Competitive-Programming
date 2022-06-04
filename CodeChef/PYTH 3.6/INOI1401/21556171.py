def countWays(c1, c2, cou, last):
    if c1 == n-1 and c2 == m-1:
        return 1
    if c1 >= n or c2 >= m or gr[c1][c2] == 0:
        return 0
    if dp[c1][c2][cou][last] != -1:
        return dp[c1][c2][cou][last]

    x = 0

    if last == 1:
        if cou < d:
            x = (x + countWays(c1 + 1, c2, cou + 1, 1)) % 20011
        x = (x + countWays(c1, c2 + 1, 1, 0)) % 20011
    else:
        x = (x + countWays(c1 + 1, c2, 1, 1)) % 20011
        if cou < d:
            x = (x + countWays(c1, c2 + 1, cou + 1, 0)) % 20011
    
    dp[c1][c2][cou][last] = x
    return x

n, m, d = map(int, input().split())

dp = [[[[-1] * 2 for _ in range(310)] for __ in range(310)] for ___ in range(310)]
gr = [list(map(int, input().split())) for _ in range(n)]

print(countWays(0, 0, 0, 0))
