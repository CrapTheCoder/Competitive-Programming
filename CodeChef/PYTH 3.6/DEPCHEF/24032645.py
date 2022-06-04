for _ in range(int(input())):
    n = int(input().strip())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    f = -1
    
    for i in range(n):
        if a[(i-1) % n] + a[(i+1) % n] < d[i] and d[i] > f:
            f = d[i]
            
    print(f)
