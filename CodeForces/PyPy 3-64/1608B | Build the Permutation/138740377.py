from sys import stdin
input = stdin.readline
 
 
def count(p):
    a = b = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] > p[i + 1]:
            a += 1
        if p[i - 1] > p[i] < p[i + 1]:
            b += 1
 
    return a, b
 
 
def create(r):
    beg = 1
    end = n
 
    l = []
    for i in r:
        if i == 0:
            l.append(beg)
            beg += 1
        if i == 1:
            l.append(end)
            end -= 1
 
    return l, beg, end
 
 
def solve(l):
    p, beg, end = create(l)
 
    if l[-1] == 1:
        for i in range(end, beg - 1, -1):
            p.append(i)
    else:
        for i in range(beg, end + 1):
            p.append(i)
 
    if count(p) != (a, b):
        return []
    else:
        return p
 
 
for _ in range(int(input())):
    n, a, b = map(int, input().split())
 
    if abs(a - b) > 1 or a + b + 2 > n:
        print(-1)
        continue
 
    if a > b:
        l = [(i+1) % 2 for i in range(a+b)]
    else:
        l = [i % 2 for i in range(a + b)]
 
    s1 = solve([0] + l + [0])
    s2 = solve([0] + l + [1])
    s3 = solve([1] + l + [0])
    s4 = solve([1] + l + [1])
 
    if s1: print(*s1)
    elif s2: print(*s2)
    elif s3: print(*s3)
    elif s4: print(*s4)
    else:
        print(-1)