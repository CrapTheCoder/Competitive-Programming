n = int(input())
a = [input() for _ in range(n)]
 
c = 0
 
for i in range(1, n-1):
    for j in range(1, n-1):
        if a[i][j] == 'X':
            c += a[i-1][j-1] == a[i+1][j-1] == a[i-1][j+1] == a[i+1][j+1] == 'X'
 
print(c)