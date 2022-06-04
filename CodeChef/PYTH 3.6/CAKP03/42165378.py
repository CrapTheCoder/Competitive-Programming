from itertools import groupby

for _ in range(int(input())):
    s = input()
    t = input()

    j = 0
    for i in s:
        while (j < len(t)) and (t[j] != i):
            j += 1

        if j == len(t):
            print('NO')
            break

    else:
        print('YES')
