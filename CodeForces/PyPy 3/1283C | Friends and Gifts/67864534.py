n = int(input())
a = list(map(int, input().split()))
 
l1 = []
l2 = set(range(1, n + 1))
 
for i in range(n):
    if a[i] == 0:
        l1.append(i)
 
    else:
        l2.remove(a[i])
 
m = len(l1)
l2 = sorted(l2)
 
while any(l1[i] + 1 == l2[i] for i in range(m)):
    l2 = l2[1:] + [l2[0]]
 
for i in range(len(l1)):
    a[l1[i]] = l2[i]
 
print(*a)