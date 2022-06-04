from bisect import bisect

n = int(input())
a = list(map(int, input().split()))

l = []

s = 0

for i in range(n):
    b = bisect(l, a[i])

    s += i - b

    l.insert(b, a[i])

print(s)