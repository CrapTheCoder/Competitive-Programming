class Dict(dict):
def __missing__(self, key):
return float('-inf')

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

dp = [Dict() for _ in range(n+1)]
dp[0][n*100] = 0

for i in range(1, n+1):
s = a[i] - b[i]*k
for j in range(n*200, -1, -1):
dp[i][j] = max(dp[i-1][j], dp[i-1][j-s] + a[i])

print(dp[n][n*100] or -1)