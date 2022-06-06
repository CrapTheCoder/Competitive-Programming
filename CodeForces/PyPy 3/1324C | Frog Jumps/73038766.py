for _ in range(int(input())):
    s = input().strip() + 'R'
    n = len(s)
 
    dr = -1
 
    d = 0
 
    for i, j in enumerate(s):
        if j == 'R':
            d = max(d, i - dr)
            dr = i
 
    print(d)