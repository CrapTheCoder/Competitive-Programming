from bisect import bisect_left as bs
 
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
 
    p = [a[0]]
    for i in range(1, n):
        p.append(p[-1] + a[i])
 
    for _ in range(m):
        x = int(input())
        r = bs(p, x) + 1
        print(-1 if r > n else r)