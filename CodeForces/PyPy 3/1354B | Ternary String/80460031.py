from sys import stdin
input = stdin.readline
 
def min(x, y): return x if x < y else y
def max(x, y): return x if x > y else y
 
for _ in range(int(input())):
    s = list(map(int, input().strip()))
 
    d = {}
 
    mini = float('inf')
 
    for j, i in enumerate(s):
        d[i] = j
 
        if (1 in d) and (2 in d) and (3 in d):
            if i == 1:
                mini = min(mini, j - min(d[2], d[3]) + 1)
            if i == 2:
                mini = min(mini, j - min(d[1], d[3]) + 1)
            if i == 3:
                mini = min(mini, j - min(d[1], d[2]) + 1)
 
    if mini == float('inf'):
        print(0)
    else:
        print(mini)