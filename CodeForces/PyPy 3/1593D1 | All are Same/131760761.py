from math import gcd
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if len(set(a)) == 1:
        print(-1)
        continue
 
    else:
        g = a[1] - a[0]
        for i in range(2, n):
            g = gcd(g, a[i] - a[i-1])
 
        print(g)