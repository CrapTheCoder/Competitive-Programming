def rep(n, s):
    global c
 
    if n <= s:
        return n
 
    for i in range(s+1, n):
        l.append((i, i+1))
        c += 1
 
    on = n
    while n > 1:
        n = -(-n // s)
        l.append((on, s))
        c += 1
 
    return s
 
for _ in range(int(input())):
    l = []
    n = int(input())
    c = 0
 
    n = rep(n, 59)
    n = rep(n, 8)
    n = rep(n, 2)
 
    print(len(l))
    for i in l:
        print(*i)