n = int(input())
a = list(map(int, input().split()))

c0 = c1 = c2 = 0

for i in a:
    if i % 4 == 0:
        c0 += 1
    elif i % 2:
        c1 += 1
    else:
        c2 += 1

if c2:
    if c1 <= c0:
        print('Yes')
    else:
        print('No')
else:
    if c1 <= c0 + 1:
        print('Yes')
    else:
        print('No')