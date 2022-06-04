from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

def solve(i, j, c=0):
    if i > j:
        return 0

    if (i, j) in dp:
        return dp[i, j]

    x0 = solve(i+1, j, c^1)
    x1 = solve(i, j-1, c^1)

    if c == 0:
        y = 1 << (j - i)
        x0 += a[i] * y
        x1 += a[j] * y

    dp[i, j] = x0 + x1
    return dp[i, j]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = {}

    total = solve(0, n-1)
    print(total / (1 << n))
