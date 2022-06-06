from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = set()
 
    for _ in range(n):
        l, r = map(int, input().split())
        a.add((l, r))
 
    f = [(1, n)]
 
    for l, r in f:
        if l == r:
            print(l, r, r)
            continue
 
        for x, y in a:
            if l == x and y+1 == r:
                print(l, r, r)
                f.append((l, r-1))
                break
 
            if x-1 == l and y == r:
                print(l, r, l)
                f.append((l+1, r))
                break
 
            if l == x and (y+2, r) in a:
                print(l, r, y+1)
                f.append((x, y))
                f.append((y+2, r))
                break
 
            if r == y and (l, x-2) in a:
                print(l, r, x-1)
                f.append((x, y))
                f.append((l, x-2))
                break
 
    print()