for _ in range(int(input())):
    n = int(input())
    s = input()
 
    if s.count('M') * 2 != s.count('T'):
        print('NO')
        continue
 
    m = [i for i, j in enumerate(s) if j == 'M']
    t = [i for i, j in enumerate(s) if j == 'T']
    
    for c in range(n // 3):
        if not t[c] < m[c] < t[c + n//3]:
            print('NO')
            break
        
    else:
        print('YES')