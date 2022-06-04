for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    ma = mi = 0
    
    for i in range(n-1, -1, -1):
        if a[i] >= 0:
            ma += 1
        else:
            break
        
    if ma == n:
        mi = n
    else:
        mi = n - ma
    
    print(ma, mi)

    