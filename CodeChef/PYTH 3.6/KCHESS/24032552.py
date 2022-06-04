# Author: Dancing Monkey | Created: 06.DEC.2018

from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = []
    
    for _ in range(n):
        a, b = map(int, input().split())
        l.append((a+1, b+2))
        l.append((a+1, b-2))
        l.append((a-1, b+2))
        l.append((a-1, b-2))
        l.append((a+2, b+1))
        l.append((a+2, b-1))
        l.append((a-2, b+1))
        l.append((a-2, b-1))

    a, b = map(int, input().split())

    x = []
    x.append((a+1, b+1) in l)
    x.append((a+1, b+0) in l)
    x.append((a+1, b-1) in l)
    x.append((a+0, b+1) in l)
    x.append((a+0, b+0) in l)
    x.append((a+0, b-1) in l)
    x.append((a-1, b+1) in l)
    x.append((a-1, b+0) in l)
    x.append((a-1, b-1) in l)

    print('NO' if False in x else 'YES')
