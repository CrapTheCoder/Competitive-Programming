from heapq import *
 
for _ in  range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    p = list(range(1, n + 1))
 
    u = [0] * n
 
    x = [a[0]]
 
    if a[0] == 1:
        heappop(p)
    else:
        u[a[0] - 1] = 1
 
    for i in range(1, n):
        if a[i] == a[i-1]:
            m = heappop(p)
 
            if m > a[i - 1]:
                print(-1)
                break
 
            while u[m - 1]:
                m = heappop(p)
 
                if m > a[i - 1]:
                    print(-1)
                    break
 
            else:
                u[m - 1] = 1
                x.append(m)
                continue
 
            break
 
        else:
            if a[i] < a[i - 1]:
                print(-1)
                break
 
            u[a[i] - 1] = 1
            x.append(a[i])
 
    else:
        print(*x)