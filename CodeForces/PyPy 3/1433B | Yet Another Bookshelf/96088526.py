for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    z = 0
    l = -1
 
    c = 0
 
    for i in range(n):
        if a[i] == 0:
            z += 1
 
        else:
            if l != -1:
                c += z
 
            l = i
 
            z = 0
 
    print(c)