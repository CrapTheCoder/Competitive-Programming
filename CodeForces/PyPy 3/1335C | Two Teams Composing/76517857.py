from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    c = sorted(Counter(a).values())
 
    maxi = 0
 
    for i in range(len(c)):
        maxi = max(maxi, min(c[i], i), min(c[i] - 1, i + 1))
 
    print(maxi)