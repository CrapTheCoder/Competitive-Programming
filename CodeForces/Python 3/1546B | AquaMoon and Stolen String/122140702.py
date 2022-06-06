from collections import Counter
 
for _ in range(int(input())):
    n, m = map(int, input().split())
 
    cm = [Counter() for _ in range(m)]
    for _ in range(n):
        s = input()
        for i in range(m):
            cm[i][s[i]] += 1
 
    for _ in range(n-1):
        s = input()
        for i in range(m):
            cm[i][s[i]] -= 1
 
    print(''.join(list(i.elements())[0] for i in cm), flush=True)