for _ in range(int(input())):
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(n)))
 
    l, r = 0, n-1
 
    while l < r:
        m = (l+r) // 2
        s0 = sum(a[i][0] for i in range(m+1))
 
        flag = True
 
        for i in range(m+1, n):
            if a[i][0] <= s0:
                s0 += a[i][0]
            else:
                flag = False
                break
 
        if flag:
            r = m
        else:
            l = m+1
 
    f = []
    for i in range(l, n):
        f.append(a[i][1] + 1)
 
    print(len(f))
    print(*sorted(f))