for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    x = 0
    
    for i in range(n):
        x += a[i]
        x -= k
        
        if x < 0:
            print('NO', i + 1)
            break
    else:
        print('YES')