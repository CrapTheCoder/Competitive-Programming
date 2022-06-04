for _ in range(int(input())):
    x, y = map(int, input().split())

    if x > y:
        print(x - y)
        
    else:
        c = 0
        while x < y:
            x += 2
            c += 1
        
        if x != y:
            x -= 1
            c += 1
            
        print(c)