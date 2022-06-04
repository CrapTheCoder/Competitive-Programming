for _ in range(int(input())):
    input()
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    res = []
    x = y = 0
 
    for i in range(n+m):
        if x < n and a[x] == 0:
            res.append(a[x])
            x += 1
            k += 1
            continue
 
        if y < m and b[y] == 0:
            res.append(b[y])
            y += 1
            k += 1
            continue
 
        if x < n and a[x] <= k:
            res.append(a[x])
            x += 1
            continue
 
        if y < m and b[y] <= k:
            res.append(b[y])
            y += 1
            continue
 
        print(-1)
        break
 
    else:
        print(*res)