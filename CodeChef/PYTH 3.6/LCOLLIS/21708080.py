for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(map(int, list(input()))) for i in range(n)]

    c = 0

    for i in range(m):
        x = 0

        for j in range(n):
            x += grid[j][i]

        c += x * (x - 1) // 2

    print(c)
