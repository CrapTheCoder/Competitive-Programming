n, m = map(int, input().split())

ls = []
rs = []

for _ in range(m):
    l, r = map(int, input().split())
    ls.append(l)
    rs.append(r)

print(max(0, min(rs) - max(ls) + 1))