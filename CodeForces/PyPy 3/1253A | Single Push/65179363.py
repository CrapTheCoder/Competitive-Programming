for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    l = 0
 
    f = g = False
 
    for i in range(n):
        d = b[i] - a[i]
 
        if d:
            if g:
                print('NO')
                break
 
            f = True
 
            if d < 0 or l and l != d:
                print('NO')
                break
 
            l = d
        else:
            if f:
                g = True
 
            l = 0
    else:
        print('YES')