from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    c = Counter(a)
 
    l = []
 
    for i in sorted(c): l.append(i)
    for i in c: l.extend([i] * (c[i] - 1))
 
    print(*l)