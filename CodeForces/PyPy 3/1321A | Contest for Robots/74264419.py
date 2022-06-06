n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
x1 = set(i for i in range(n) if a[i])
x2 = set(i for i in range(n) if b[i])
 
x = len(x1.difference(x2))
 
if x == 0:
    print(-1)
    exit()
 
s1 = sum(a)
s2 = sum(b)
 
ms = 1
 
while s1 <= s2:
    s1 += x
    ms += 1
 
print(ms)