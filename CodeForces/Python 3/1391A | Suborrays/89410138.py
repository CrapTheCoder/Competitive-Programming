from functools import reduce
 
def _or(x, y):
    return x | y
 
for _ in range(int(input())):
    n = int(input())
    a = list(range(1, n+1))
    
    print(*a)