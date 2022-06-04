from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

s = 0
for i in c:
    s += -(-c[i] // 2)

print(s)