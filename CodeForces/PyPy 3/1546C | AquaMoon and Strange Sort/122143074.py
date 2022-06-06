for _ in range(int(input())):
    n = int(input())
 
    a = list(map(int, input().split()))
    b = sorted(a.copy())
 
    d1 = {}
    d2 = {}
 
    for i, j in enumerate(a):
        d1[j] = d1.get(j, [0, 0])
        d1[j][i % 2] += 1
 
    for i, j in enumerate(b):
        d2[j] = d2.get(j, [0, 0])
        d2[j][i % 2] += 1
 
    for i in d1:
        c0 = d1[i][0] - d2[i][0]
        c1 = d1[i][1] - d2[i][1]
 
        if c0 or c1:
            print('NO')
            break
 
    else:
        print('YES')