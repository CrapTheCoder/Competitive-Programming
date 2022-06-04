for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split())) + [float('inf')]
 
    b = []
 
    i = 1
    o = a[0]
    c = [o]
 
    while i < n:
        if a[i] > o:
            b.extend(c[::-1])
            o = a[i]
            c = [o]
 
        else:
            c.append(a[i])
 
        i += 1
 
    b.extend(c[::-1])
    print(*b[::-1])