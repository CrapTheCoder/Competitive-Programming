for _ in range(int(input())):
    s = input()
    
    if len(s) < 3:
        print("Dynamic")
    else:
        a = sorted(s.count(i) for i in set(s))
        
        f = True
        
        for i in range(len(a) - 2):
            if a[i+2] == a[i+1] + a[i]:
                f = True
            else:
                f = False
            
            
        print ('Dynamic' if f else 'Not')
            
    