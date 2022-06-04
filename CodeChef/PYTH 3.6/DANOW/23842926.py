n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [a[i] * b[i] for i in range(n)]

d = [0]

for i in range(n):
    d.append(c[i] + d[-1])

for _ in range(q):
    l, r = map(int, input().split())

    print(d[r] - d[l-1])
