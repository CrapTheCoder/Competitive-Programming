for _ in range(int(input())):
    a, b, n = map(int, input().split())
    c = 0
 
    a, b = sorted([a, b])
 
    while a <= n and b <= n:
        a += b
        a, b = b, a
        c += 1
 
    print(c)