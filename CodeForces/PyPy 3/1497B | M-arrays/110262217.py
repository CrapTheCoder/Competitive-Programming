for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    md = [0] * k
    for i in a:
        md[i%k] += 1
 
    c = 0
    if md[0] > 0:
        c += 1
 
    l, r = 1, k-1
 
    while l <= r:
        if l != r:
            x = min(md[l], md[r])
            md[l] -= x
            md[r] -= x
            if x > 0:
                c += 1
 
                if md[l] > 0: md[l] -= 1
                if md[r] > 0: md[r] -= 1
 
            c += md[l] + md[r]
 
        else:
            if md[l] > 0:
                c += 1
 
        l += 1
        r -= 1
 
    print(c)