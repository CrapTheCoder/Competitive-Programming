for _ in range(int(input())):
    n = int(input())
    
    l = len(bin(n)) - 2
    
    x = 1
    
    for i in range(l):
        if n ^ x <= n:
            print(x, n ^ x)
            break
        
        x *= 2
        
    else:
        print(-1)