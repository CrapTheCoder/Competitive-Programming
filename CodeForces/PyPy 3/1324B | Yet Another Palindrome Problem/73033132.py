from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    C = Counter(a)
 
    if any(i > 2 for i in C.values()):
        print('YES')
        continue
 
    d = {}
 
    for i in range(n):
        d[a[i]] = d.get(a[i], -1)
 
        if d[a[i]] == -1:
            d[a[i]] = i
            continue
 
        j = d[a[i]]
 
        if i - j - 1 > 0:
            print('YES')
            break
    else:
        print('NO')