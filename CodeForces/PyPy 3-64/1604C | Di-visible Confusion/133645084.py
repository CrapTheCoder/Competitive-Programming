from math import gcd
 
def lcm(x, y):
    return x * y // gcd(x, y)
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    l = 1
    for i in range(n):
        if l < 10 ** 10:
            l = lcm(l, i+2)
 
        if a[i] % l == 0:
            print('NO')
            break
 
    else:
        print('YES')