for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            a[i - 1][j] = a[i - 1][j] + max(a[i][j], a[i][j + 1])

    print(a[0][0])