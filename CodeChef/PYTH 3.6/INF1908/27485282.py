for _ in range(int(input())):
    n, k = map(int, input().split())
    n = list(map(int, list(str(n))))
    
    n[-1] = (k + n[-1]) % 10
    
    print(*n, sep='')
