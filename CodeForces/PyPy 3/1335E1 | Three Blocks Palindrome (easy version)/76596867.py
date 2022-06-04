from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    s = Counter(a)
 
    x = [(i, j) for i in s for j in s if i != j]
 
    maxi = 0
 
    for i, j in x:
        size = 0
 
        l = 0
        r = n - 1
 
        while True:
            while a[l] != i: l += 1
            while a[r] != i: r -= 1
 
            if l >= r:
                break
 
            size += 1
 
            maxi = max(maxi, size * 2 + a[l:r].count(j))
 
            l += 1
            r -= 1
 
    print(max(maxi, max(s.values())))