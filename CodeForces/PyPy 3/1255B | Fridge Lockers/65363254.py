for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
 
    x = sorted(zip(a, list(range(n))))
 
    if n == 2 or m < n:
        print(-1)
    else:
        c = 0
 
        l = []
 
        for i in range(m):
            l.append((x[i % n][1] + 1, x[(i+1) % n][1] + 1))
            c += x[i % n][0] + x[(i+1) % n][0]
 
        print(c)
 
        for i in l:
            print(*i)