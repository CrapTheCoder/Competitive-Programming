from math import ceil
 
for _ in range(int(input())):
    n, g, b = map(int, input().split())
 
    if b <= g:
        print(n)
        continue
 
    x = ceil(n / 2)
 
    a = (g + b) * ((x - 1) // g) + (x - 1) % g + 1
 
    print(max(n, a))