n = int(input())
a = t = 0

l = []

for _ in range(n):
    av, tv = map(int, input().split())
    a += av

    l.append((2*av + tv, av, tv))

l.sort(reverse=True)

for j, i in enumerate(l):
    a -= l[j][1]
    t += l[j][1] + l[j][2]

    if a < t:
        print(j+1)
        break