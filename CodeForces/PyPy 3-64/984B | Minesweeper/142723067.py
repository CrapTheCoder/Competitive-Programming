n, m = map(int, input().split())
l = [list(input()) for _ in range(n)]
 
for i in range(n):
    for j in range(m):
        c = 0
        if i-1 >= 0 and l[i-1][j] == '*': c += 1
        if i+1 < n and l[i+1][j] == '*': c += 1
        if j-1 >= 0 and l[i][j-1] == '*': c += 1
        if j+1 < m and l[i][j+1] == '*': c += 1
        if i-1 >= 0 and j-1 >= 0 and l[i-1][j-1] == '*': c += 1
        if i+1 < n and j-1 >= 0 and l[i+1][j-1] == '*': c += 1
        if i-1 >= 0 and j+1 < m and l[i-1][j+1] == '*': c += 1
        if i+1 < n and j+1 < m and l[i+1][j+1] == '*': c += 1
 
        if l[i][j] == '.':
            if c != 0:
                print('NO')
                exit()
 
            continue
 
        if l[i][j] == '*':
            continue
 
        if c != int(l[i][j]):
            print('NO')
            exit()
 
print('YES')