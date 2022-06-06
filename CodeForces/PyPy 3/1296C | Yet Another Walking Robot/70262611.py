INF = float('inf')
 
for i in range(int(input())):
    n = int(input())
    s = input()
 
    x, y = (0, 0)
    d = {(0, 0): 0}
 
    m = INF
    mi = -1
 
    for i in range(n):
        if s[i] == 'L': x -= 1
        if s[i] == 'R': x += 1
 
        if s[i] == 'U': y += 1
        if s[i] == 'D': y -= 1
 
        if (x, y) in d:
            if m > (i + 1) - d[x, y]:
                m = (i + 1) - d[x, y]
                mi = i + 1
 
        d[x, y] = i + 1
 
    if mi == -1:
        print(-1)
    else:
        print(mi - m + 1, mi)