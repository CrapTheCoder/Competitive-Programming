n, p, k = map(int, input().split())
t = sorted(map(int, input().split()))

cnt = 1
last = t[0]
cur = 1

for i in t[1:]:
    if (i - last > k) or (cur >= p):
        last = i
        cur = 1
        cnt += 1
        continue

    cur += 1

print(cnt)