from bisect import bisect

MAX = 10 ** 5 + 20

ps = [True] * MAX
ps[0] = ps[1] = False

p = []

for i in range(2, MAX):
    if ps[i]:
        p.append(i)
        for j in range(i*i, MAX, i):
            ps[j] = False

n = int(input())
a = list(map(int, input().split()))
c = 0

for i in a:
    c += min(abs(i - p[bisect(p, i)-1]), abs(p[bisect(p, i)] - i))

print(c)
