for _ in range(int(input())):
    n = int(input())
    g = [input() for _ in range(n)]
 
    x1 = g[0][1] + g[1][0]
    x2 = g[-1][-2] + g[-2][-1]
 
    if x1[0] == x1[1] == x2[0] == x2[1]:
        print(2)
        print(1, 2)
        print(2, 1)
        continue
 
    if (x1[0] != x2[0]) == (x1[1] != x2[1]):
        if x1[0] == x1[1] and x2[0] == x2[1]:
            print(0)
            continue
 
        if x1[0] == x2[1] and x2[0] == x1[1]:
            print(2)
            print(1, 2)
            print(n, n-1)
            continue
 
        if x1[0] == x2[0] and x1[1] == x2[1]:
            print(2)
            print(1, 2)
            print(n-1, n)
            continue
 
    if x1[0] == x1[1] == x2[0]:
        print(1)
        print(n, n-1)
        continue
 
    if x1[0] == x1[1] == x2[1]:
        print(1)
        print(n-1, n)
        continue
 
    if x2[0] == x2[1] == x1[0]:
        print(1)
        print(1, 2)
        continue
 
    if x2[0] == x2[1] == x1[1]:
        print(1)
        print(2, 1)
        continue