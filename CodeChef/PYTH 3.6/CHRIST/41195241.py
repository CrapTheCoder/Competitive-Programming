N = 10000013
p = [True] * N

ps = [1]
for i in range(2, N):
    if p[i]:
        ps.append(i)
        for j in range(i*i, N, i):
            p[j] = False

n = int(input())
l = []
for i in ps[:n]:
    l.append(n*i)

print(*l)
