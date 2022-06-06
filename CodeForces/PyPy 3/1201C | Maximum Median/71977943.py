n, k = map(int, input().split())
a = sorted(map(int, input().split()))
 
if n == 1:
    print(a[0] + k)
    exit()
 
y = n // 2
ans = a[y]
 
while True:
    for y in range(y + 1, n):
        if a[y] != ans:
            break
    else:
        r = n - n // 2
        ans += k // r
        print(ans)
 
        break
 
    r = y - n // 2
 
    if ans + k // r >= a[y]:
        k -= (a[y] - ans) * r
        ans = a[y]
    else:
        ans += k // r
        print(ans)
 
        break