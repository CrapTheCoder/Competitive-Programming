from math import factorial
from itertools import permutations

n = int(input())
a = tuple(sorted(map(lambda x: tuple(sorted(x)), input().split())))
b = tuple(sorted(map(lambda x: tuple(sorted(x)), input().split())))

if a != b:
    print(0)
else:
    if n == 1:
        print(1)
    else:
        c = 0
    
        for i in permutations(a):
            if a == b:
                c += 1
    
        print(c - factorial(len(set(a))) + 1)
