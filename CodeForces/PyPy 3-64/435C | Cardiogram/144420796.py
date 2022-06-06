n = int(input())
a = list(map(int, input().split()))
pic = [[' '] * 3000 for i in range(3000)]
 
x, y = 1500, 0
for i in range(n):
    for j in range(a[i]):
        if not i % 2:
            pic[x][y] = '/'
            x -= 1
        else:
            pic[x][y] = '\\'
            x += 1
 
        y += 1
 
    if not i % 2:
        x += 1
    else:
        x -= 1
 
for i in range(3000):
    if not ''.join(pic[i][:y]).isspace():
        print(*pic[i][:y], sep='')