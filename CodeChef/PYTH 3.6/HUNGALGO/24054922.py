for _ in range(int(input())):
    n = int(input())
    lr = [list(map(int, input().split())) for __ in range(n)]
    lc = [[lr[j][i] for j in range(n)] for i in range(n)]

    if all(0 in i for i in lr) and all(0 in i for i in lc):
        print('YES')
    else:
        print('NO')