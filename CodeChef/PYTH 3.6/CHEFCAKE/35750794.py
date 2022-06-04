from math import factorial as f

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(sum((i * f(n-1)) * (10 ** j) for i in a for j in range(n)))
