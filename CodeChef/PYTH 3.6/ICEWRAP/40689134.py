n = int(input())

cur = [n] * (2 * n - 1)
l = [cur.copy()]

for i in range(1, n):
    cur[i:-i] = [n-i] * len(cur[i:-i])
    l.append(cur.copy())

for i in l:
    print(*i)

for i in l[:-1][::-1]:
    print(*i)