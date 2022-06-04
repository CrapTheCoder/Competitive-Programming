from sys import stdin
input = stdin.readline

from collections import Counter

for _ in range(int(input())):
    s = input()
    x1, y1 = map(int, input().split())

    c = Counter(s)

    for _ in range(int(input())):
        x2, y2 = map(int, input().split())

        d1 = 'L'
        d2 = 'D'

        if x1 < x2: d1 = 'R'
        if y1 < y2: d2 = 'U'

        if c[d1] >= abs(x1 - x2) and c[d2] >= abs(y1 - y2):
            print('YES', abs(x1 - x2) + abs(y1 - y2))
        else:
            print('NO')