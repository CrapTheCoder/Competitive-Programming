from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [input().strip() for _ in range(n)]
 
    mini = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            s = 0
            for k in range(m):
                s += abs(ord(l[i][k]) - ord(l[j][k]))
 
            mini = min(mini, s)
 
    print(mini)