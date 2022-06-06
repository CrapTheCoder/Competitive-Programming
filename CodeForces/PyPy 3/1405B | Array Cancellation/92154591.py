for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    c = s = 0
 
    for i in range(n-1, -1, -1):
        if a[i] < 0:
            s += abs(a[i])
 
        else:
            c += min(s, a[i])
            s = max(s - a[i], 0)
 
    print(s)