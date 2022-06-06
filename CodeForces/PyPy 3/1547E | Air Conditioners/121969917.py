for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    a, b = zip(*sorted(zip(a, b)))
 
    x = [-1] * n
    for i in range(k):
        x[a[i] - 1] = b[i]
 
    pre = [float('inf')] * n
 
    start = a[0] - 1
    mi = float('inf')
    mii = -1
 
    for i in range(start, n):
        if x[i] != -1:
            if mi > x[i]:
                mi = x[i]
                mii = i
 
        pre[i] = min(pre[i], mi)
        mi += 1
 
    suf = [float('inf')] * n
    start = a[-1] - 1
    mi = float('inf')
    mii = -1
 
    for i in range(start, -1, -1):
        if x[i] != -1:
            if mi > x[i]:
                mi = x[i]
                mii = i
 
        suf[i] = min(suf[i], mi)
        mi += 1
 
    res = []
    for i in range(n):
        res.append(min(pre[i], suf[i]))
 
    print(*res)