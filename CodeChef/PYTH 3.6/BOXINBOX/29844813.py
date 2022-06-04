from sys import stdin

INF = float('inf')

n = int(stdin.readline())

a = [list(map(int, stdin.readline().split())) for _ in range(n)]

m = []

for i in range((n + 1) // 2):
    mini = INF

    mini = min(min(a[i][i:n-i]), min(a[n-i-1][i:n-i]))

    for j in range(i+1, n-i-1):
        mini = min(mini, a[j][i], a[j][n-i-1])

    m.append(mini)

print(sum(m))
