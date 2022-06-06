def query(i):
    assert 0 <= i < n
    print(f'? {i+1}', flush=True)
    return int(input()) - 1
 
def done(p):
    print('!', *[i+1 for i in p], flush=True)
 
for _ in range(int(input())):
    n = int(input())
 
    cyc = []
    vis = set()
 
    query(0)
 
    for i in range(n):
        if i in vis:
            continue
 
        cur = []
        c = query(i)
 
        vis.add(c)
 
        while True:
            if len(vis) == n:
                cur.append(c)
                break
 
            d = query(i)
            vis.add(d)
            cur.append(d)
 
            if c == d:
                break
 
        cyc.append((cur[::-1], i))
 
    else:
        p = [-1] * n
 
        for a, i in cyc:
            b = a[1:] + a[:1]
            for k in range(len(a)):
                p[b[k]] = a[k]
 
        done(p)