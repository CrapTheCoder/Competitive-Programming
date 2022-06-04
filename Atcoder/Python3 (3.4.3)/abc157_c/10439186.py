n, m = map(int, input().split())

l = [-1] * n

for _ in range(m):
    s, c = map(int, input().split())
    s -= 1

    if l[s] == -1:
        l[s] = c

    elif l[s] != c:
        print(-1)
        exit()

if n > 1 and l[0] == 0:
    print(-1)
    exit()

if l[0] == -1:
    if n == 1:
        l[0] = 0
    else:
        l[0] = 1

for i in range(n):
    if l[i] == -1:
        l[i] = 0

print(*l, sep='')