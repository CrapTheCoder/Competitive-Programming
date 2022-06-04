for _ in range(int(input())):
    n = int(input())
    
    s = input()
    u = input()
    
    c = 0
    
    f = True
    
    for i, j in zip(s, u):
        if f:
            if j == 'N':
                continue
            if i == j:
                c += 1
            if i != j:
                f = False
        else:
            f = True
    
    print(c)