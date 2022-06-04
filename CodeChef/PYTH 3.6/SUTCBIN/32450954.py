from collections import Counter

n = int(input())
a = list(map(int, input().split()))

d = {}

for j, i in enumerate(a):
    if i not in d:
        d[i] = j

c = Counter(a)

x = sorted(set(a), key=d.get)

for i in x:
    print(i + c[i], end=' ')

print()
