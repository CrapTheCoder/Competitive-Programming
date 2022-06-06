def count(m):
    if m <= k:
        s = m * (m+1) // 2
 
    else:
        s = k * (k+1) // 2
 
        c = (2*k-1) - m
        s += k * (k-1) // 2 - c * (c+1) // 2
 
    return s
 
for _ in range(int(input())):
    k, x = map(int, input().split())
 
    l, r = 0, 2*k-1
    while l+1 < r:
        m = (l+r) // 2
 
        # print(m, l, r, count(m))
        if count(m) < x:
            l = m
        else:
            r = m
 
    print(r)
 
"""
 
n
n-1
n-2
.
.
.
 
 
 
"""