from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    c = Counter(a)
    l = sorted(c.values())
 
    mini = float('inf')
 
    s = [0]
    for i in l[::-1]:
        s.append(s[-1] + i)
    s.reverse()
 
    p = 0
    for i in range(len(l)):
        mini = min(mini, p + s[i+1] - l[i] * (len(l)-i-1))
        p += l[i]
 
    print(mini)