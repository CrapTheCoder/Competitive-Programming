n = int(input())
a = sorted(map(int, input().split()))
 
l1 = []
l2 = []
 
for i in a:
    if not l1:
        l1.append(i)
    else:
        if l1[-1] == i:
            l2.append(i)
        else:
            l1.append(i)
 
if all(l1[i] > l1[i-1] for i in range(1, len(l1))) and \
    all(l2[i] > l2[i-1] for i in range(1, len(l2))):
    print('YES')
    print(len(l2))
    print(*l2)
    print(len(l1))
    print(*l1[::-1])
else:
    print('NO')