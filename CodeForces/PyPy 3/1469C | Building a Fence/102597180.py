for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    l, h = a[0], a[0]
 
    for i in range(1, n):
        nl = max(a[i], l-k+1)
        nh = min(a[i] + k-1, h+k-1)
        l, h = nl, nh
 
        if (l > h) or (l > a[i] + k-1):
            print('NO')
            break
 
    else:
        if l <= a[-1] <= h:
            print('YES')
        else:
            print('NO')