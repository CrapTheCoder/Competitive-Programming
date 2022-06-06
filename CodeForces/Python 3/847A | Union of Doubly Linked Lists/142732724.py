n = int(input())
 
f = [-1] * n
e = [-1] * n
 
for i in range(n):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
 
    if l != -1:
        f[i] = l
 
    if r != -1:
        e[i] = r
 
vis = [False] * n
 
ls = []
for i in range(n):
    if vis[i] or (f[i] != -1 and e[i] != -1):
        continue
 
    if e[i] == -1:
        cur = [i]
        vis[i] = True
        while f[i] != -1:
            i = f[i]
            vis[i] = True
            cur.append(i)
 
        ls.append(cur)
 
for i in range(len(ls) - 1):
    if f[ls[i][-1]] == -1:
        f[ls[i][-1]] = ls[i+1][0]
        e[ls[i+1][0]] = ls[i][-1]
 
for i, j in zip(f, e):
    print(i+1, j+1)