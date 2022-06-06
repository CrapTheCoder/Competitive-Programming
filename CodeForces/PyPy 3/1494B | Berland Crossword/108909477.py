def solve():
    for i in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:
                for l in [0, 1]:
                    c = [0, 0, 0, 0]
                    if i: c[0] += 1; c[3] += 1
                    if j: c[1] += 1; c[0] += 1
                    if k: c[2] += 1; c[1] += 1
                    if l: c[3] += 1; c[2] += 1
 
                    g = f.copy()
                    g[0] -= c[0]
                    g[1] -= c[1]
                    g[2] -= c[2]
                    g[3] -= c[3]
 
                    if all(0 <= x <= n-2 for x in g):
                        print('YES')
                        return
 
    print('NO')
 
 
for _ in range(int(input())):
    n, u, r, d, l = map(int, input().split())
    f = [u, r, d, l]
 
    solve()