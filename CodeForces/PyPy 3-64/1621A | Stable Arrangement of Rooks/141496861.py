from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n, k = map(int, input().split())
 
    s = [['.'] * n for _ in range(n)]
 
    c = 0
    for i in range(k):
        if c >= n:
            print(-1)
            break
 
        s[c][c] = 'R'
        c += 2
    else:
        print('\n'.join(''.join(x) for x in s))