x = input()
y = input()
n, m = len(x), len(y)

lcs = [[-1] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if 0 in [i, j]: lcs[i][j] = 0
        elif x[i-1] == y[j-1]: lcs[i][j] = lcs[i-1][j-1] + 1
        else: lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[n][m])
