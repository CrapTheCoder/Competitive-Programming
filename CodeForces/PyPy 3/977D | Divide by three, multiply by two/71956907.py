n = int(input())
a = list(map(int, input().split()))
 
g = [-1] * n
 
for i in range(n):
    for j in range(n):
        if a[i] * 2 == a[j]: g[i] = j
        if a[j] * 3 == a[i]: g[i] = j
 
cur = g.index(-1)
 
result = [cur]
 
while cur in g:
    cur = g.index(cur)
    result.append(cur)
 
print(*[a[i] for i in result[::-1]])