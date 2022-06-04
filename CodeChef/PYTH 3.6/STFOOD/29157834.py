for _ in range(int(input())):
    n = int(input())
    m = float('-inf')
    
    for _ in range(n):
        s, p, v = map(int, input().split())
        s += 1
        
        m = max(v * (p // s), m)
        
    print(m)