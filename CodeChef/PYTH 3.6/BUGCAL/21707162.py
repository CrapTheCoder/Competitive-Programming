for _ in range(int(input())):
    a, b = map(int, input().split())
    
    x = 0
    y = []
    
    while a or b:
        y += [(a % 10 + b % 10) % 10]
        a //= 10
        b //= 10
        
    for i in y[::-1]:
        x *= 10
        x += i
        
    print(x)
