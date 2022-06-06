for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    c = 0
    i = 0
 
    while i+1 < len(a):
        if a[i+1] > a[i]:
            if a[i+1] > 2 * a[i]:
                a.insert(i+1, 2*a[i])
                c += 1
 
        if a[i+1] < a[i]:
            if a[i] > 2 * a[i+1]:
                a.insert(i+1, -(-a[i] // 2))
                c += 1
        i += 1
 
    print(c)