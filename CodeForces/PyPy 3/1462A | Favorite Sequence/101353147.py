for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    b = [0] * n
 
    l, r, i = 0, n-1, 0
 
    while l <= r:
        if not i % 2:
            b[i] = a[l]
            l += 1
 
        else:
            b[i] = a[r]
            r -= 1
 
        i += 1
 
    print(*b)