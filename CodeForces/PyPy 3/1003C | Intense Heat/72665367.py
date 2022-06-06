n, k = map(int, input().split())
a = list(map(int, input().split()))
 
maxi = float('-inf')
 
for i in range(n - k + 1):
    s = sum(a[i:i+k])
    c = 0
 
    cur_maxi = s / k
 
    for j in range(i+k, n):
        s += a[j]
        c += 1
 
        cur_maxi = max(cur_maxi, s / (k + c))
 
    maxi = max(maxi, cur_maxi)
 
print(maxi)