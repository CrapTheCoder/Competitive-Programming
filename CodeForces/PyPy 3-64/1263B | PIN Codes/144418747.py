from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    a = [list(input()) for _ in range(n)]
 
    c = 0
    for i in range(n):
        if a.count(a[i]) > 1:
            for j in range(4):
                for k in range(10):
                    a[i][j] = str(k)
                    if a.count(a[i]) == 1:
                        c += 1
                        break
                else:
                    continue
 
                break
 
    print(c)
    for i in a:
        print(*i, sep='')