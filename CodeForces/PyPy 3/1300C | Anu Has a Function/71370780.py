n = int(input())
a = list(map(int, input().split()))
 
l = [bin(i)[2:].zfill(32) for i in a]
 
ind = -1
 
for i in range(32):
    c = 0
 
    flag = False
 
    for j in range(n):
        if l[j][i] == '1':
            if flag:
                ind = -1
                flag = False
                break
 
            flag = True
            ind = j
 
    if flag:
        break
 
if ind == -1:
    print(*a)
else:
    print(a[ind], *(a[i] for i in range(n) if i != ind))