n, m, k = map(int, input().split())

c = 0
for i in range(n):
    t = list(map(int, input().split()))
    if sum(t[:-1]) >= m and t[-1] <= 10:
        c += 1

print(c)
