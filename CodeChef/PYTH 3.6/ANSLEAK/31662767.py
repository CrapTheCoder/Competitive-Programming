from sys import stdin
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

        c = choice(a)

        x.append(choice([i for i in range(k) if a[i] == c]))
        
    print(*l[choice(x)])
