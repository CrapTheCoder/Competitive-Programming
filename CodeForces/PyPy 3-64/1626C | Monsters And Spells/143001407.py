from sys import stdin
input = stdin.readline
 
max = lambda x, y: x if x > y else y
min = lambda x, y: x if x < y else y
 
for _ in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
 
    inc = [0] * n
    for i in range(n):
        inc[i] = (k[i] - h[i] + 1, k[i])
 
    t = 0
    rem = []
    for i in range(n-2, -1, -1):
        if inc[i+1][0] <= inc[i][1]:
            inc[i] = (min(inc[i][0], inc[i+1][0]), max(inc[i][1], inc[i+1][1]))
            rem.append(inc[i+1])
 
    for s, e in inc:
        r = e-s+1
        t += r * (r+1) // 2
 
    for s, e in rem:
        r = e-s+1
        t -= r * (r+1) // 2
 
    # print(inc, rem)
    print(t)