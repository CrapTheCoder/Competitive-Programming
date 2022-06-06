for _ in range(int(input())):
    s = input()
 
    l = -1
 
    x = 0
 
    for i in range(len(s)):
        if s[i] == '1':
            if l != -1:
                x += i - l - 1
            
            l = i
 
    print(x)