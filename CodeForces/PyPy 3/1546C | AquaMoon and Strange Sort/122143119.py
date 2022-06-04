for _ in range(int(input())):
    n = int(input())
 
    a = list(map(int, input().split()))
    b = sorted(a.copy())
 
    d1 = {}
 
    for i, j in enumerate(a):
        d1[j] = d1.get(j, [0, 0])
        d1[j][i % 2] += 1
 
    for i, j in enumerate(b):
        d1[j][i % 2] -= 1
 
    for i in d1:
        if d1[i][0] or d1[i][1]:
            print('NO')
            break
 
    else:
        print('YES')