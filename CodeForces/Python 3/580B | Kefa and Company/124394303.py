n, d = map(int, input().split())
 
l = []
for _ in range(n):
    m, s = map(int, input().split())
    l.append((m, s))
 
l.sort()
 
b = 0
maxi = 0
cnt = 0
 
for a in range(n):
    while (b < n) and (l[b][0] < l[a][0] + d):
        cnt += l[b][1]
        b += 1
 
    maxi = max(maxi, cnt)
    cnt -= l[a][1]
 
print(maxi)