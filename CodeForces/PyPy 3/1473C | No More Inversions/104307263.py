from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(range(k, k - (n-k) - 1, -1))
 
    d = []
    for i in range(1, l[-1]):
        d.append(i)
 
    print(*(d + l))