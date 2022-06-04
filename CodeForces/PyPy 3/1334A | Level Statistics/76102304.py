for _ in range(int(input())):
    n = int(input())
 
    lp, lc = 0, 0
 
    ans = 'YES'
 
    for _ in range(n):
        p, c = map(int, input().split())
 
        x = p - lp
        y = c - lc
 
        if x < 0 or y < 0:
            ans = 'NO'
 
        if x < y:
            ans = 'NO'
 
        lp, lc = p, c
 
    print(ans)