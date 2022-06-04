from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())
    a, b = bin(n+1).count('1'), bin(m+1).count('1')
    
    if a == b: print(0, 0)
    if a < b: print(1, b-a)
    if a > b: print(2, a-b)