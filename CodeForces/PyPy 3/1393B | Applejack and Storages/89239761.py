from collections import Counter
 
n = int(input())
a = list(map(int, input().split()))
 
c = Counter(a)
t = {}
 
for i in c:
    t[c[i]] = t.get(c[i], 0) + 1
 
for q in range(int(input())):
    f, x = input().split()
    x = int(x)
 
    t[c[x]] = t.get(c[x], 0) - 1
 
    if f == '-': c[x] -= 1
    if f == '+': c[x] += 1
 
    t[c[x]] = t.get(c[x], 0) + 1
 
    r1 = False
    r2 = 0
 
    for i in sorted(t):
        if i >= 4:
            if t[i] >= 1:
                if not r1:
                    r2 += ((i * t[i]) - 4) // 2
                else:
                    r2 += (i * t[i]) // 2
 
                r1 = True
 
        elif i >= 2:
            r2 += t[i]
 
    if r1 and r2 >= 2:
        print('YES')
    else:
        print('NO')