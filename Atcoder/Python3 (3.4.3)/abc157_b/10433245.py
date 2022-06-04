a = [list(map(int, input().split())) for _ in range(3)]

mark = [[False] * 3 for _ in range(3)]

n = int(input())

for _ in range(n):
    x = int(input())

    for i in range(3):
        for j in range(3):
            if a[i][j] == x:
                mark[i][j] = True

a = mark

for i in range(3):
    if all(a[i][j] == True for j in range(3)) or all(a[j][i] == True for j in range(3)):
        print('Yes')
        break
else:
    if all(a[i][i] == True for i in range(3)) or all(a[i][3-i-1] == True for i in range(3)):
        print('Yes')
    else:
        print('No')