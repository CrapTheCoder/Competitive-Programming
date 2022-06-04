for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]

    u = d = l = r = -1

    for i in range(n):
        if any(a[i][j] == '1' for j in range(m)):
            u = i
            break

    for i in range(n-1, -1, -1):
        if any(a[i][j] == '1' for j in range(m)):
            d = i
            break

    for j in range(m):
        if any(a[i][j] == '1' for i in range(n)):
            l = j
            break

    for j in range(m-1, -1, -1):
        if any(a[i][j] == '1' for i in range(n)):
            r = j
            break

    flag = False
    for i in range(u, d+1):
        for j in range(l, r+1):
            if a[i][j] != '1':
                print('NO')
                flag = True
                break

        if flag:
            break

    if not flag:
        print('YES')