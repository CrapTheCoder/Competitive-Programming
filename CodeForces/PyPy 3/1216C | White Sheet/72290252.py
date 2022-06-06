def overlap():
    ax1, ay1 = x3, y4
    ax2, ay2 = x4, y3
 
    bx1, by1 = x5, y6
    bx2, by2 = x6, y5
 
    return (ax1 <= bx2) and (ax2 >= bx1) and (ay1 >= by2) and (ay2 <= by1)
 
def full_cover(xb, yb, xt, yt):
    return (xb <= x1) and (yb <= y1) and (xt >= x2) and (yt >= y2)
 
def f1(x, y): return (x <= x1) and (y <= y1)
def f2(x, y): return (x <= x1) and (y >= y2)
def f3(x, y): return (x >= x2) and (y >= y2)
def f4(x, y): return (x >= x2) and (y <= y1)
 
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())
 
edges = (((x1, y1), (x2, y2), (x1, y2), (x2, y1)),
         ((x3, y3), (x4, y4), (x3, y4), (x4, y3)),
         ((x5, y5), (x6, y6), (x5, y6), (x6, y5)))
 
if full_cover(x3, y3, x4, y4) or full_cover(x5, y5, x6, y6):
    print('NO')
    exit()
 
if (f1(x3, y3) or f1(x5, y5)) and (f2(x3, y4) or f2(x5, y6)) and \
   (f3(x4, y4) or f3(x6, y6)) and (f4(x4, y3) or f4(x6, y5)):
 
    if overlap():
        print('NO')
    else:
        print('YES')
else:
    print('YES')