n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

tss = []

for i in range(n):
    ts = 0

    for j in range(n):
        if i != j:
            ts |= a[i][j]

    tss.append(ts)

print(sum(tss))