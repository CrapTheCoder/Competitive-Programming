n, x = map(int, input().split())
a = sorted(map(int, input().split()))
 
c = 0
for i in range(n):
    c += max(1, x - i) * a[i]
 
print(c)