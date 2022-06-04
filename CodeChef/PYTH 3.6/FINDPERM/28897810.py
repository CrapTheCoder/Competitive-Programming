n = int(input())
a = list(map(int, input().split()))

l = []

for i in range(n):
    l.insert(i - a[i], i + 1)

print(*l)