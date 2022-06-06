for _ in range(int(input())):
    n, m, a, b = map(int, input().split())
 
    if a * n != b * m:
        print('NO')
        continue
 
    g = [[0] * m for _ in range(n)]
 
    cur = 0
 
    for i in range(n):
        for _ in range(a):
            g[i][cur] = 1
            cur = (cur + 1) % m
 
    print('YES')
 
    for row in g:
        print(*row, sep='')