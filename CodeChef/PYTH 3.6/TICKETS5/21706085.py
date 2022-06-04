for t in range(int(input())):
    s = input()
    
    a = s[::2]
    b = s[1::2]
    
    if len(set(a)) == len(set(b)) == 1 and s[0] != s[1]:
        print('YES')
    else:
        print('NO')
