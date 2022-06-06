s = input()
n = len(s)
c = s.count('o')
 
if c == 0:
    print('YES')
    
else:
    if (n - c) % c == 0:
        print('YES')
    else:
        print('NO')