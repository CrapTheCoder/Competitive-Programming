from math import sqrt
 
def largest(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
 
    return n
 
for _ in range(int(input())):
    n, k = map(int, input().split())
 
    if n % 2 == 0:
        print(n + 2 * k)
        continue
 
    print(n + largest(n) + 2 * (k-1))