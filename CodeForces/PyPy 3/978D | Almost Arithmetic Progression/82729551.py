n = int(input())
b = list(map(int, input().split()))
 
if n == 1:
    print(0)
    exit()
 
mini = float('inf')
 
for x in (0, 1, -1):
    for y in (0, 1, -1):
        a = b.copy()
        a[0] += x
        a[1] += y
 
        c = abs(x) + abs(y)
 
        for i in range(2, n):
            if abs((a[1] - a[0]) - (a[i] - a[i-1])) > 1:
                break
 
            c += abs((a[1] - a[0]) - (a[i] - a[i-1]))
            a[i] += (a[1] - a[0]) - (a[i] - a[i-1])
 
        else:
            mini = min(mini, c)
 
if mini == float('inf'):
    print(-1)
else:
    print(mini)