from sys import stdin
from collections import Counter

input = stdin.readline

MAX = 10 ** 5 + 10
p = [i for i in range(MAX)]

for i in range(2, int(MAX ** 0.5) + 1):
    if p[i] == i:
        for j in range(i*i, MAX, i):
            p[j] = i

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c1 = Counter()
    for i in range(n):
        x = a[i]
        while x != 1:
            c1[p[x]] += 1
            x //= p[x]

    c2 = Counter()
    for i in range(n):
        x = a[i]
        while x != 1:
            c1[p[x]] -= 1
            c2[p[x]] += 1
            x //= p[x]

        for j in c1:
            if c1[j] > 0 and c2[j] > 0:
                break
        else:
            print(i+1)
            break
