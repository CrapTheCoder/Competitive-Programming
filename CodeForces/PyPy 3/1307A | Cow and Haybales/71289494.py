for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
 
    for i in range(1, n):
        if d - (i * a[i]) >= 0:
            d -= i * a[i]
            a[0] += a[i]
        else:
            x = d // i
 
            a[0] += min(a[i], x)
            break
 
    print(a[0])