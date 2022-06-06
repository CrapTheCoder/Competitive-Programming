def solve(a):
    m = float('-inf')
    m1 = 0
 
    for i in range(len(a)):
        m1 = m1 + a[i]
 
        if m < m1:
            m = m1
 
        if m1 < 0:
            m1 = 0
 
    return m
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if sum(a) > max(solve(a[:-1]), solve(a[1:])):
        print('YES')
    else:
        print('NO')