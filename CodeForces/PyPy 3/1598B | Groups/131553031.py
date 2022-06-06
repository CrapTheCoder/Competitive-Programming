for _ in range(int(input())):
    n = int(input())
 
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
 
    flag = False
    for i in range(5):
        for j in range(i+1, 5):
            s1 = s2 = 0
 
            flag2 = False
            for k in range(n):
                if l[k][i] != l[k][j]:
                    if l[k][i]: s1 += 1
                    if l[k][j]: s2 += 1
                else:
                    if l[k][i] == 0:
                        flag2 = True
                        break
 
            if (not flag2) and (s1 <= n // 2) and (s2 <= n // 2):
                print('YES')
                flag = True
                break
 
        if flag:
            break
 
    if not flag:
        print('NO')