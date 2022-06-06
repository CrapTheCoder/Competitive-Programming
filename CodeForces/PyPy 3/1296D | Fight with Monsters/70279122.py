from math import ceil
 
n, a, b, k = map(int, input().split())
h = list(map(int, input().split()))
 
p = 0
 
l = []
 
for i in h:
    x = i % (a + b)
 
    win = True
 
    if x == 0 or x - a > 0:
        win = False
 
    if win:
        p += 1
        continue
 
    if x == 0:
        l.append(ceil(b / a))
    else:
        l.append(ceil((x - a) / a))
 
l.sort()
 
for i in l:
    if k - i >= 0:
        k -= i
        p += 1
    else:
        break
 
print(p)