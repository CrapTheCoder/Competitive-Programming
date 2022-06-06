for _ in range(int(input())):
    n, m = map(int, input().split())
 
    d1 = {}
    d2 = {}
 
    a = []
 
    for i in range(n):
        a.append(list(map(int, input().split())))
 
        for j in range(m):
            d1[i-j] = d1.get(i-j, 0) + a[i][j]
            d2[i+j] = d2.get(i+j, 0) + a[i][j]
 
    maxi = 0
    for i in range(n):
        for j in range(m):
            maxi = max(maxi, d1[i-j] + d2[i+j] - a[i][j])
 
    print(maxi)