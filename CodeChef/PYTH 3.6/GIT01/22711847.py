for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(input()) for i in range(n)]
    
    x = y = 0
    
    for i in range(n):
        for j in range(m):
            if (i+j) % 2:
                if a[i][j] == 'G': x += 3
                if a[i][j] == 'R': y += 5
            else:
                if a[i][j] == 'G': y += 3
                if a[i][j] == 'R': x += 5

    print(min(x, y))