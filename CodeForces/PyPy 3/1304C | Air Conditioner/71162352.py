from sys import stdin
 
input = stdin.readline
 
def sects(x1, y1, x2, y2):
    return x1 <= y2 and x2 <= y1
 
for _ in range(int(input())):
    n, m = map(int, input().split())
 
    x = {}
 
    for _ in range(n):
        t, l, h = map(int, input().split())
 
        x[t] = x.get(t, []) + [(l, h)]
 
    flag = False
 
    a = [(0, m, m)]
 
    for k, v in x.items():
        l = max(i[0] for i in v)
        h = min(i[1] for i in v)
 
        if l > h:
            print('NO')
            flag = True
 
            break
 
        a.append((k, l, h))
 
    if not flag:
        a.sort()
 
        le = len(a)
 
        for i in range(le):
            ct = 0
 
            x1, y1 = a[i][1], a[i][2]
 
            for j in range(i+1, le):
                ct += a[j][0] - a[j-1][0]
 
                x2, y2 = a[j][1] - ct, a[j][2] + ct
 
                if not (sects(x1, y1, x2, y2) or sects(x2, y2, x1, y1)):
                    print('NO')
                    flag = True
                    break
 
            if flag:
                break
 
        if not flag:
            print('YES')