from collections import deque
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    mini = float('inf')
    q = deque()
 
    for i in range(n):
        if a[i] < mini:
            q.appendleft(a[i])
            mini = a[i]
        else:
            q.append(a[i])
 
    print(*list(q))