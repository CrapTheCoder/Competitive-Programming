for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    t = 0
    mini = cur = a[0]
 
    for i in range(n-1, 0, -1):
        t += max(a[i-1] - a[i], 0)
 
    print(t)