INF = float('inf')

def f(x, y):
    return abs(int(bin(x)[2:] + bin(y)[2:], 2) - int(bin(y)[2:] + bin(x)[2:], 2))

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    d = {}
    
    for i in a:
        l = len(bin(i)[2:])
        d[l] = d.get(l, [INF, -INF])
        if i < d[l][0]: d[l][0] = i
        if i > d[l][1]: d[l][1] = i
    
    m = 0
    
    for i in d.keys():
        for j in d.keys():
            m = max(m, f(d[i][0], d[j][1]), f(d[i][1], d[j][0]))
    
    print(m)