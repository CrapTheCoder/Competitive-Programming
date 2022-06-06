n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
 
c = {}
 
for i in range(n):
    c[a[i]] = c.get(a[i], []) + [i]
 
v = 0
 
for i, j in c.items():
    if len(j) > k:
        print('NO')
        exit()
 
    for x in j:
        b[x] = v + 1
 
        v += 1
        v %= k
 
print('YES')
print(*b)