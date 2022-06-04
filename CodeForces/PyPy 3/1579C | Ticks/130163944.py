for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = [list(input()) for _ in range(n)][::-1]
 
    new = [['.'] * m for _ in range(n)]
 
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                h = 0
                while (i+h < n) and (j-h) >= 0 and (j+h) < m and a[i+h][j-h] == a[i+h][j+h] == '*':
                    h += 1
 
                if h > k:
                    for f in range(h):
                        new[i+f][j-f] = new[i+f][j+f] = '*'
 
    if new == a:
        print('YES')
    else:
        print('NO')