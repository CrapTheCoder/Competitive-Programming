for _ in range(int(input())):
    n = int(input())
    p = list(map(lambda i: int(i) - 1, input().split()))
 
    b = [0] * n
 
    for i in range(n):
        if b[i]:
            continue
 
        j = p[i]
 
        y = [i]
        c = 1
 
        while j != i:
            y.append(j)
            j = p[j]
            c += 1
 
        for i in y:
            b[i] = c
 
    print(*b)