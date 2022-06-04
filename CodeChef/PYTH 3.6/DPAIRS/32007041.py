n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

da = {a[i]: i for i in range(n)}
db = {b[i]: i for i in range(m)}

sa = sorted(a)
sb = sorted(b)

for i in range(m):
    print(da[sa[0]], db[sb[i]])

for i in range(1, n):
    print(da[sa[i]], db[sb[m-1]])
