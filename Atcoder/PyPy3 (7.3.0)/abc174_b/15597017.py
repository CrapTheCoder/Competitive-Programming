from math import sqrt

n, d = map(int, input().split())

c = 0

for _ in range(n):
    x, y = map(int, input().split())
    
    if sqrt(x*x + y*y) <= d:
        c += 1

print(c)