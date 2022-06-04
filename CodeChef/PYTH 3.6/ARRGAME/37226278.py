from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    t = []

    for i in groupby(a):
        i = list(i)

        if i[0] == 0:
            t.append(len(list(i[1])))

    t.sort()

    if len(t) == 0:
        print('No')
        continue

    if len(t) == 1:
        if t[-1] % 2:
            print('Yes')
        else:
            print('No')

        continue

    if t[-1] % 2 == 0:
        print('No')
        continue

    if t[-1] // 2 < t[-2]:
        print('No')
        continue

    print('Yes')