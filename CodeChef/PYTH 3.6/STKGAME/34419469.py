n = int(input())

l = []
lc = False
c = 0

for i in range(n):
    a, h = map(int, input().split())

    l.append([a, h])

    if i == 0:
        c += 1
        lc = True
        continue

    if lc:
        if a - l[-2][0] <= h:
            lc = False

        else:
            c += 1
            lc = True

        continue

    if a - l[-2][0] > l[-2][1]:
        c += 1
        l[-2][0] += l[-2][1]
        l[-2][1] = 0

    if a - l[-2][0] <= h:
        lc = False
    else:
        c += 1
        lc = True

if not lc:
    c += 1

print(c)
