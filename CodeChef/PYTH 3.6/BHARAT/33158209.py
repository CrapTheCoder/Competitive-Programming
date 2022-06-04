MOD = 10 ** 9 + 7

n, k = map(int, input().split())

pre = [[0] * k for _ in range(n+1)]

for i in range(1, n+1):
    pre[i][0] = i
    for j in range(1, k):
        pre[i][j] = (pre[i-1][j] + pre[i][j-1]) % MOD

print(pre[n][k-1])