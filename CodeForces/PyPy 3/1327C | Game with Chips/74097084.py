n, m, k = map(int, input().split())
 
sx = sy = -1
 
for _ in range(k):
    csx, csy = tuple(map(int, input().split()))
    sx = max(sx, csx)
    sy = max(sy, csy)
 
ans = ''
 
ans += 'U' * (sx-1)
ans += 'L' * (sy-1)
 
for i in range(n):
    if i % 2 == 0:
        ans += 'R' * (m-1)
    else:
        ans += 'L' * (m-1)
 
    if i != n-1:
        ans += 'D'
 
print(len(ans))
print(ans)