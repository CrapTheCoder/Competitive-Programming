for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    
    if n == m == 1:
        print(x)
        continue
    
    if x * 2 <= y:
        print(x * n * m)
        continue
    
    if x >= y:
        print(-(-(n*m) // 2) * y)
        continue
    
    if (n*m) % 2:
        print((n*m // 2) * y + x)
        continue
    
    print((n*m // 2) * y)
