from sys import stdin
input = stdin.readline
 
def solve(a, d=0):
    if not a:
        return
 
    maxi = max(a)
    m = a.index(maxi)
    sol[maxi] = d
 
    solve(a[:m], d+1)
    solve(a[m+1:], d+1)
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sol = {}
 
    solve(a)
 
    l = []
    for i in a:
        l.append(sol[i])
 
    print(*l)