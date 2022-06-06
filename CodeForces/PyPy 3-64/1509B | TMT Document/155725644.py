for _ in range(int(input())):
    n = int(input())
    s = input()
 
    if s.count('M') * 2 != s.count('T'):
        print('NO')
        continue
 
    m = []
    t = []
    for i, j in enumerate(s):
        if j == 'M':
            m.append(i)
        else:
            t.append(i)
 
    c = 0
    for i in m:
        if not t[c] < i < t[c + n//3]:
            print('NO')
            break
 
        c += 1
        
    else:
        print('YES')