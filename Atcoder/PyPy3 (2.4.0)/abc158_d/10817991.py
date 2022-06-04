from collections import deque

s = input()

d = deque(list(s))

rev = False

for i in range(int(input())):
    tp = input().split()

    if tp[0] == '1':
        rev = not rev
    else:
        f, c = tp[1:]

        if rev:
            f = '12'[f == '1']

        if f == '1':
            d.appendleft(c)
        else:
            d.append(c)

if rev:
    print(*list(d)[::-1], sep='')
else:
    print(*list(d), sep='')