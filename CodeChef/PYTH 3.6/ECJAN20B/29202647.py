from math import ceil

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    
    x = k // (n + m)
    
    ans = x * n
    
    if k - x * (n + m) < n:
        ans += k - x * (n + m)
    else:
        ans += n
    
    print(ans)