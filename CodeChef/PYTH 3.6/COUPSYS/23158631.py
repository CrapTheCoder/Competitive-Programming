for _ in range(int(input())):
    n = int(input())
    p, q, r = [], [], []
    
    for i in range(n):
        c, l, x = map(int, input().split())
        if l == 1: p.append((x, c))
        elif l == 2: q.append((x, c))
        else: r.append((x, c))
    
    p, q, r = sorted(p, reverse=True), sorted(q, reverse=True), sorted(r, reverse=True)
    
    print(p[0][0], min([y if p[0][0] == x else 101 for x, y in p]))
    print(q[0][0], min([y if q[0][0] == x else 101 for x, y in q]))
    print(r[0][0], min([y if r[0][0] == x else 101 for x, y in r]))