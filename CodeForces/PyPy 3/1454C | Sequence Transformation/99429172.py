from collections import deque
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if len(set(a)) == 1:
        print(0)
        continue
 
    d = {}
 
    for i, j in enumerate(a):
        d[j] = d.get(j, []) + [i]
 
    mini = float('inf')
    for j in d.values():
        c = 0
        j = [-1] + j + [n]
 
        for i in range(1, len(j)):
            f = j[i] - j[i-1] - 1
            if f > 0:
                c += 1
 
        mini = min(mini, c)
 
    print(mini)