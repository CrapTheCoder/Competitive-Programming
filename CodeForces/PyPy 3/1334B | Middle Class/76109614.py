for _ in range(int(input())):
    n, x = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
 
    s = 0
 
    ans = 0
 
    for i in range(n):
        s += a[i]
 
        if s // (i+1) >= x:
            ans += 1
 
    print(ans)