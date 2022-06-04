for _ in range(int(input())):
    n, k = map(int, input().split())
    c = 0
    
    for i in range(n):
        t, d = map(int, input().split())
        
        if t >= k:
            c += (t - k) * d
            k = 0
        else:
            k = k - t

    print(c)
