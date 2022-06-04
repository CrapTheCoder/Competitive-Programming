for _ in range(int(input())):
    n = int(input()) 
    a = list(map(int, input().split())) 

    x = list(set(a))
    
    if n == 1:
        print(-1)

    elif len(x) > 2:
        print(-1)
        
    elif len(x) == 1:
        if x[0] == n-1:
            print(0)
        elif x[0] == 0:
            print(n)
        else:
            print(-1)
    
    else:
        p = max(x)
        f = a.count(p)
        
        if p == a.count(min(x)):
            print(f)
        else:
            print(-1)
