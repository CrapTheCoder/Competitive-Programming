from sys import stdin
input = stdin.readline
 
min = lambda x, y: x if x < y else y
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
 
    suf = [0] * (n+1)
    for i in range(n-1, -1, -1):
        suf[i] = suf[i+1] + a[i]
 
    s = suf[0]
 
    mini = float('inf')
    for i in range(n):
        c = a[0] + suf[n-i]
        x = i+1
        rc = s - c
 
        maxi = min(a[0], (k - rc) // x)
        mini = min(mini, (a[0] - maxi) + x-1)
 
    print(mini)