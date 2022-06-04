n, k = map(int, input().split())
 
if k >= n * 2:
    print(0)
else:
    a = n // 2 - (n // 2 - k // 2)
 
    if k > n:
        a = n - a
    if k <= n and k % 2 == 0:
        a -= 1
 
    print(a)