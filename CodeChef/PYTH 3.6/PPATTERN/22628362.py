for _ in range(int(input())):
    n = int(input())
    l = list(range(n)) + list(range(n - 1, 0, -1))
    
    for i in range(1, n + 1):
        d = i * (i + 1) // 2
        print(d, end=' ')
        
        x = 1

        while x < n:
            d += l[i + x - 1]
            print(d, end=' ')
            x += 1

        print()