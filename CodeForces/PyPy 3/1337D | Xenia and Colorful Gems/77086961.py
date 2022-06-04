def solve(r, g, b):
    nr, ng, nb = len(r), len(g), len(b)
 
    ri = bi = 0
 
    mini = float('inf')
 
    for gi in range(ng):
        while ri < nr and r[ri] <= g[gi]:
            ri += 1
 
        if ri != 0:
            ri -= 1
 
        while bi < nb and b[bi] < g[gi]:
            bi += 1
 
        if bi == nb:
            bi -= 1
 
        x, y, z = r[ri], g[gi], b[bi]
 
        mini = min(mini, (x-y) ** 2 + (y-z) ** 2 + (z-x) ** 2)
 
    return mini
 
def main():
    for _ in range(int(input())):
        input()
 
        r = sorted(map(int, input().split()))
        g = sorted(map(int, input().split()))
        b = sorted(map(int, input().split()))
 
        mini = min(
            solve(r, g, b),
            solve(r, b, g),
            solve(g, r, b),
            solve(g, b, r),
            solve(b, r, g),
            solve(b, g, r),
        )
 
        print(mini)
 
main()