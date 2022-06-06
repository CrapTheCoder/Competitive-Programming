n = int(input())
a = list(map(int, input().split()))
 
f = 0
for i in range(n-1, -1, -1):
    if a[i] != a[0]:
        f = i
        break
 
l = n-1
for i in range(n):
    if a[i] != a[-1]:
        l = i
        break
 
print(max(f, n - l - 1))