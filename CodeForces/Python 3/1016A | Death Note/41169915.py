n, m = map(int, input().split())
lis = list(map(int, input().split()))
 
x = ''
dum = 0
 
for i in lis:
    dum += i
    a = dum // m
    dum -= (m * a)
 
    x += str(a) + ' '
 
print(x[:-1])