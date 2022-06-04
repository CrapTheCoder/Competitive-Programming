from itertools import combinations

ps = []
for i in range(1, 6+1):
    ps.extend(combinations(list(range(6)), i))

n, q = map(int, input().split())
p = list(map(int, input().split()))
b = list(map(int, input().split()))

x = [[] for _ in range(6)]

for i, j in zip(p, b):
    x[j-1].append(i)

ts = {i: sorted(sum((x[j] for j in i), []), reverse=True) for i in ps}

for _ in range(q):
    t, k = map(int, input().split())
    f = tuple(map(lambda x: int(x) - 1, input().split()))

    try:
        print(ts[f][k-1])
    except:
        print(-1)
