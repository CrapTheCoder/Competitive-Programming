from itertools import groupby

for _ in range(int(input())):
    s = input()
    
    x = groupby(s)
    
    l = ''
    
    for i, j in x:
        l += i
        l += str(len(list(j)))
    
    print('YES' if len(l) < len(s) else 'NO')