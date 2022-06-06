MAX = 15000
 
for _ in range(int(input())):
    a, b, c = map(int, input().split())
 
    ans = float('inf')
 
    aa, bb, cc = 0, 0, 0
 
    for xa in range(1, MAX + 1):
        for xb in range(xa, MAX + 1, xa):
            for xc in range(xb, MAX + 1, xb):
                if abs(a - xa) + abs(b - xb) + abs(c - xc) < ans:
                    ans = abs(a - xa) + abs(b - xb) + abs(c - xc)
                    aa, bb, cc = xa, xb, xc
 
    print(ans)
    print(aa, bb, cc)