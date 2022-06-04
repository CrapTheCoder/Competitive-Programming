from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    s = sum(a) / n
    c = Counter()
 
    d = 0
    for i in a:
        d += c[2*s - i]
        c[i] += 1
 
    print(d)