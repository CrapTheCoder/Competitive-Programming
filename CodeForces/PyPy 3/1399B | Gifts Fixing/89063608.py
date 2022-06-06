for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ma = min(a)
    mb = min(b)
    
    c = 0
    
    for x, y in zip(a, b):
        if x > ma and y > mb:
            z = min(x - ma, y - mb)
            c += z
            x -= z
            y -= z
        
        c += (x - ma) + (y - mb)
    
    print(c)