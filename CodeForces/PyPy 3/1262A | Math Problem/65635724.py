for _ in  range(int(input())):
    n = int(input())
    x = []
 
    m1 = -1
    m2 = float('inf')
 
    for __ in range(n):
        l, r = map(int, input().split())
        m1 = max(m1, l)
        m2 = min(m2, r)
 
    print(max(0, m1 - m2))