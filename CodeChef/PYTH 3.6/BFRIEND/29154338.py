for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    f = list(map(int, input().split()))
    
    m = float('inf')
    
    for i in f:
        m = min(m, abs(b - i) + abs(i - a))
    
    print(m + c)