from collections import deque
 
for _ in range(int(input())):
    k, n = map(int, input().split())
    a = deque(sorted(map(int, input().split())))
    s = 0
 
    while a:
        d = []
 
        for _ in range((k-1) // 2):
            d.append(a.popleft())
 
        for _ in range(k - (k-1) // 2):
            d.append(a.pop())
 
        d.sort()
        s += d[(len(d) + 1) // 2 - 1]
 
    print(s)