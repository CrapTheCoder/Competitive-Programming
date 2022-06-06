for _ in range(int(input())):
    w, h, n = map(int, input().split())
 
    c = 0
 
    while w % 2 == 0:
        c += 1
        w //= 2
 
    while h % 2 == 0:
        c += 1
        h //= 2
 
    print('YES' if 2 ** c >= n else 'NO')