for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    r = n
    for r in range(n-2, -1, -1):
        if a[r] < a[r+1]:
            r += 1
            break
 
    l = 0
 
    for i in range(1, r):
        if a[i] < a[i-1]:
            l = i
 
    print(l)