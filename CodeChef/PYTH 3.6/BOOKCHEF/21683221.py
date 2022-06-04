n, m = map(int, input().split())
a = input().split()

special = []
normal = []

for i in range(m):
    f, p, s = input().split()

    if f in a:
        special.append([int(p), s])
    else:
        normal.append([int(p), s])

print(*[i[1] for i in sorted(special, reverse=True) + sorted(normal, reverse=True)], sep='\n')