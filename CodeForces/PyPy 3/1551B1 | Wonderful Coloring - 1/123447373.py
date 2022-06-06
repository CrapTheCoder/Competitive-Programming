from collections import Counter
 
for _ in range(int(input())):
    s = input().strip()
 
    f = 0
    t = 0
 
    c = Counter(s)
    for i in c:
        if c[i] > 1:
            t += 1
        else:
            f += 1
 
    print(f // 2 + t)