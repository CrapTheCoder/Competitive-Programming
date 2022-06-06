def solve(c):
    if len(str(c)) > n:
        return float('inf')
 
    if c in dp:
        return dp[c]
 
    if len(str(c)) == n:
        return 0
 
    mini = float('inf')
    for y in str(c):
        if c * int(y) != c:
            d = solve(c * int(y)) + 1
            if d < mini:
                mini = d
 
    dp[c] = mini
    return mini
 
n, x = map(int, input().split())
dp = {}
 
r = solve(x)
print(r if r != float('inf') else -1)