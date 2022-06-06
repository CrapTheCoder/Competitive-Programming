n = int(input())
 
mp = {}
 
for _ in range(n):
    a, b = map(int, input().split())
    mp[a] = mp.get(a, 0) + 1
    mp[b] = mp.get(b, 0) - 1
 
cur = 0
maxi = 0
maxiy = 0
 
for i in sorted(mp):
    cur += mp[i]
 
    if cur > maxi:
        maxi = cur
        maxiy = i
 
print(maxiy, maxi)