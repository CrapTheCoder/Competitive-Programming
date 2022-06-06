from math import sqrt, ceil
 
def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
 
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
 
    m = max(a)
 
    if x < m:
        if x in a:
            print(1)
        else:
            print(2)
    else:
        print(ceil(x / m))