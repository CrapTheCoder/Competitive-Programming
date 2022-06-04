INF = float('inf')

n = int(input())
a = list(map(int, input().split()))

memo = [-1] * n
memo[0] = 0

for i in range(1, n):
    memo[i] = min(abs(a[i] - a[i-1]) + memo[i-1],
                  abs(a[i] - a[i-2]) + memo[i-2] if i - 2 >= 0 else INF)

print(memo[n-1])
