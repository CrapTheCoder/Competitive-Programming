for _ in range(int(input())):
    n = int(input())
    s = 0
    
    for i in range(n):
        p, q, d = map(int, input().split())
        s += q * p * (d ** 2) / 10000
        
    print(format(s, 'f'))