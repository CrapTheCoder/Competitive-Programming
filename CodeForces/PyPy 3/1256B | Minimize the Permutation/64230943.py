for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

x = [(i, i+1) for i in range(n - 1)]

d = sorted(i + 1 for i in range(n) if a[i] - 1 != i)
l = len(d)

ce = 0

while x and ce < l:
f = 0
ind = a.index(d[ce])

while (ind-1, ind) in x and a[ind-1] > a[ind]:
a[ind - 1], a[ind] = a[ind], a[ind - 1]
x.remove((ind-1, ind))

ind -= 1

ce += 1

print(*a)