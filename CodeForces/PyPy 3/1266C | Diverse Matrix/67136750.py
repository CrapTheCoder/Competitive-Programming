r, c = map(int, input().split())
 
if r == c == 1:
    print(0)
    exit()
 
if c == 1:
    print(*range(2, r + 2))
    exit()
 
if r == 1:
    print(*range(2, c + 2))
    exit()
 
ri = list(range(1, r + 1))
cj = list(range(r + 1, r + c + 1))
 
for i in range(r):
    for j in range(c):
        print(ri[i] * cj[j], end=' ')
 
    print()