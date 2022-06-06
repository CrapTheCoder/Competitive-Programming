from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input().strip()
 
    c = sorted((j, i) for i, j in enumerate(a) if s[i] == '0')
    d = sorted((j, i) for i, j in enumerate(a) if s[i] == '1')
 
    a = [-1] * n
 
    f = 1
 
    for j, i in c:
        a[i] = f
        f += 1
 
    for j, i in d:
        a[i] = f
        f += 1
 
    print(*a)