n = int(input())

l = []
s = 0

for i in range(n):
    c, p, d = map(int, input().split())
    s += c
    
    l.append((p + d, c))
    
l.sort(reverse=1)

m = -1
f = 0

for i in range(n):
    f += l[i][1]
    m = max(m, f + max(l[i][0], s - f))

print(m)
