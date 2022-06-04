from sys import stdin
from collections import Counter

input = stdin.readline

from random import choice

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    l = [[] for _ in range(k)]

    x = []

    for _ in range(n):
        a = list(map(int, input().split()))

        for i in range(k):
            l[i].append(a[i])

        c = Counter(a)
        m = max(c.values())

        x.append(a.index(choice([i for i in c if c[i] == m])))

    c = Counter(x)
    m = max(c.values())

    print(*l[choice([i for i in c if c[i] == m])])
