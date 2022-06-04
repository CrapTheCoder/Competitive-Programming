from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

def solve(i, j, c=0):
    if i > j:
        return 0, 1

    if (i, j) in dp:
        return dp[i, j]

    if c == 0:
        x0, y0 = solve(i + 1, j, c ^ 1)
        x1, y1 = solve(i, j - 1, c ^ 1)

        dp[i, j] = x0 + x1 + a[i] * y0 + a[j] * y1, y0 + y1
        return x0 + x1 + a[i] * y0 + a[j] * y1, y0 + y1
    else:
        x0, y0 = solve(i + 1, j, c ^ 1)
        x1, y1 = solve(i, j - 1, c ^ 1)

        dp[i, j] = x0 + x1, y0 + y1
        return x0 + x1, y0 + y1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = {}

    total, total_count = solve(0, n-1)
    print(total / total_count)
