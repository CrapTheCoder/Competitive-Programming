for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
 
    c = g = 0
 
    for i in b:
        c += i
        g = max(g, c)
 
    f = 0
    maxi = g
    for i in a:
        f += i
        maxi = max(maxi, f+g)
 
    print(maxi)