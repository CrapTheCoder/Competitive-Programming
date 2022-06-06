for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    l = []
 
    for i in range(n):
        if a[i] % 2 != i % 2:
            l.append(a[i])
 
    oc = sum(i % 2 for i in l)
    ec = len(l) - oc
 
    if oc != ec:
        print(-1)
        continue
    else:
        print(oc)