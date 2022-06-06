n = int(input())
a = list(map(int, input().split()))
 
g = [[0] * n for _ in range(n)]
 
for i in range(n):
    for j in range(n):
        if a[i] * 2 == a[j]: g[i][j] = 1
        if a[j] * 3 == a[i]: g[i][j] = 1
 
def dfs(u, b):
    for v in range(n):
        if g[u][v]:
            if dfs(v, b + [a[v]]):
                return True
 
    if len(b) == n:
        print(*b)
        return True
 
    return False
 
for u in range(n):
    if dfs(u, [a[u]]):
        break